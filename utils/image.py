import base64
import secrets

import requests
from io import BytesIO

from PIL import Image, ImageFile
from django.contrib.admin.widgets import AdminFileWidget
from django.core.files.base import ContentFile, File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.html import format_html

from service.exceptions import ValidationError

ImageFile.LOAD_TRUNCATED_IMAGES = True


def make_thumbnail(size, image, name):
	f = BytesIO()
	if size:
		image.thumbnail(size, Image.ANTIALIAS)
	image.save(f, format=image.format if image.format else 'jpeg')
	f.seek(0)
	return InMemoryUploadedFile(f, 'ImageField', name, f'image/{image.format.lower() if image.format else "jpeg"}', f.__sizeof__(), None)


def make_thumbnail_for_s3(image, name, image_size=None):

	tmp = Image.open(BytesIO(image.read()))
	image = rotate(tmp)

	f = BytesIO()
	if image_size:
		image.thumbnail(image_size, Image.ANTIALIAS)
	image.save(f, format=image.format if image.format else 'jpeg')
	f.seek(0)
	return File(f, name=name)


def rotate(image):
	if image.format == 'MPO':
		return image
	exif = image._getexif()
	if not exif:
		return image
	exif = dict(exif.items())
	orientation = 274
	if not exif.get(orientation):
		return image

	if exif[orientation] == 3:
		image = image.rotate(180, expand=True)
	elif exif[orientation] == 6:
		image = image.rotate(270, expand=True)
	elif exif[orientation] == 8:
		image = image.rotate(90, expand=True)
	return image


def url_to_image(url, file_name=''):

	resp = requests.get(url)
	if resp.status_code != requests.codes.ok:
		return

	fp = BytesIO()
	fp.write(resp.content)
	tmp = Image.open(fp)

	return InMemoryUploadedFile(
		fp,
		'ImageField',
		file_name or url.split("/")[-1],
		f'image/{tmp.format}',
		fp.__sizeof__(),
		None
	)


def base64_to_image(image=''):
	if image:
		_format, _dataurl = image.split(';base64,')
		_filename, _extension = secrets.token_hex(20), _format.split('/')[-1]
		image_file = ContentFile(base64.b64decode(
			_dataurl), name=f"{_filename}.{_extension}")
		return image_file
	else:
		raise ValidationError({'image': 'base64 uri가 필요합니다.'})


def change_image_format(image, image_format):
	if not image:
		raise ValidationError({'image': 'image 가 필요합니다'})

	img = Image.open(image).convert("RGB")
	im_io = BytesIO()
	img.save(im_io, format=image_format)
	reformatted_image = File(
		im_io, name=f"%s.{image_format}" % image.name.split('.')[0])
	return reformatted_image


class ImageViewWidget(AdminFileWidget):
	def render(self, name, value, attrs=None, renderer=None):
		html = super().render(name, value, attrs, renderer)
		if value and getattr(value, 'url', None):
			html = format_html(
				'<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" style="object-fit: contain;"/></a>',
				value.url, str(value)) + html
		return html
