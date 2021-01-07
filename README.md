## qr转文字

这是一个 读取 剪切板中的 QR码图片，转换成文字

### 使用之前

```bash
pip install qrcode
pip install pillow
pip install pyzbar
pip install pyperclip
```

需要注意的是 pyzbar 需要 vc2008 运行库支持 , 请先安装 vc运行库

### 如何使用

**文字转图片**
复制任意一段文本，运行本程序，会自动读取剪切板内容生成QR图片码 。
生成的QR码自动保存在 D:\下，运行时请更改目录

**图片转文字**
复制QR图片吗，运行本程序，解析出来的文本会自动替换剪切板内容，粘贴即可
