import os
from math import ceil

from PIL import Image, ImageDraw, ImageFont
from loguru import logger


class CutImage:
	""" 图片批量剪切 """

	def __init__(self):
		self.ims = dict()
		self.w, self.h = None, None

	def parse(self, dirname: str):
		"""
		获取需要处理的全部图片
		:param dirname: 图片所在目录
		:return:
		"""
		fileNames = os.listdir(dirname)
		allowedFormats = "png", "jpg", "jpeg"
		im_names = list(filter(lambda x: x if str(x).split(".")[1] in allowedFormats else False, fileNames))
		list(map(lambda im_name: self.add(os.path.join(dirname, im_name)), im_names))

	def add(self, fp: str):
		"""
		获取需要处理的单张图片
		:param fp: 文件路径
		:return:
		"""
		im = Image.open(fp=fp)
		self.ims[fp] = im
		self.w, self.h = im.size
		return im

	def handle(self, x1: int | float, y1: int | float, x2: int | float, y2: int | float, saveDir: str = "imgCut",
			   counter: int = 1):
		"""
		图片剪切及保存

		:param x1: 要剪切的左上角x坐标
		:param y1: 要剪切的左上角y坐标
		:param x2: 要剪切的右下角x坐标
		:param y2: 要剪切的右下角y坐标
		:param saveDir: 保存路径
		:param counter: 计数器
		:return:
		"""
		logger.info(f"共{len(self.ims)}张图片需要剪切,正在剪切中...")
		for imName, im in self.ims.items():
			imCut = im.crop((x1, y1, x2, y2))
			loc = os.path.join(os.getcwd(), saveDir)
			os.mkdir(loc) if not os.path.exists(loc) else ...
			img_name = os.path.split(imName)[-1]
			imCut.save(os.path.join(os.getcwd(), saveDir, img_name))
			logger.info(f"第{counter}张图片剪切完成")
			counter += 1

	@staticmethod
	def get_position(fp: str, hsize: int = 20, wsize: int = 30, fill: str = 'red'):
		"""
		图片尺寸定位
		:param fp: 需要定位的图片名
		:param hsize: y方向的字体大小
		:param wsize: x 方向的字体大小
		:param fill: 字体颜色
		"""

		im = Image.open(fp=fp)
		w, h = im.size
		draw = ImageDraw.Draw(im)
		font = ImageFont.truetype(font='C:/Windows/Fonts/simhei.TTF', size=hsize)
		h_number = ceil(((h - hsize) / (hsize * 2) + 1))
		w_number = ceil(((w - wsize) / (wsize * 2) + 1))
		for i in range(w_number):
			location = (wsize * i * 2, 0)
			text = str(wsize * i * 2)
			draw.text(location, text, fill, font)
		for i in range(h_number):
			location = (0, hsize * i * 2)
			text = str(hsize * i * 2)
			draw.text(location, text, fill, font)
		return im


if __name__ == '__main__':
	ci = CutImage()
	ci.parse("img")
	ci.handle(0, 98, ci.w, ci.h)
