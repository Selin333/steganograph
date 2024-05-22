import docx
import MTK2
from docx.shared import RGBColor
from docx.enum.text import WD_COLOR_INDEX

doc = docx.Document("C:\\Users\\Godless\\Desktop\\ВКБ\\Сафарьян\\1\\variant10 (1).docx")


def run_get_spacing(run):
    rPr = run._r.get_or_add_rPr()
    spacings = rPr.xpath("./w:spacing")
    return spacings


def run_get_scale(run):
    rPr = run._r.get_or_add_rPr()
    scale = rPr.xpath("./w:w")
    return scale


def main():
    prov = False
    kod = ''
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            font_color = run.font.color.rgb
            font_size = run.font.size
            font_highlight_color = run.font.highlight_color
            font_scale = run_get_scale(run)
            font_spacing = run_get_spacing(run)
            if (font_color != RGBColor(0, 0, 0) or
                    font_size.pt != 12.0 or
                    font_highlight_color != WD_COLOR_INDEX.WHITE or
                    font_spacing or font_scale):
                for i in range(len(run.text)):
                    kod += '1'
            else:
                for i in range(len(run.text)):
                    kod += '0'

            if prov == False:
                if font_color != RGBColor(0, 0, 0):
                    print('Закодированно цветом')
                    prov = True
                if font_size.pt != 12.0:
                    print('Закодированно размером шрифта')
                    prov = True

                if font_highlight_color != WD_COLOR_INDEX.WHITE:
                    print('Закодированно цветом фона')
                    prov = True

                if font_spacing or font_scale:
                    print('Закодированно масштабом')
                    prov = True
        print(paragraph.text)


    
    while len(kod)%8!=0:
        kod += "0"
    print('Код скрытого текста:')
    print(kod)
    # print(len(kod))
    normaltext = bytes.fromhex(hex(int(kod, 2))[2:]).decode(encoding="koi8_r")
    print('Перевод в кодировку koi8 - ',normaltext[:normaltext.find('.')+1])
    normaltext = bytes.fromhex(hex(int(kod, 2))[2:]).decode(encoding="cp866")
    print('Перевод в кодировку cp866 - ',normaltext[:normaltext.find('.')+1])
    normaltext = bytes.fromhex(hex(int(kod, 2))[2:]).decode(encoding="cp1251")
    print('Перевод в кодировку cp1251 - ',normaltext[:normaltext.find('.')+1])
    normaltext = MTK2.MTK2_decode(kod)
    print('Перевод в кодировку MTK2 - ',normaltext)


if __name__ == '__main__':
    main()