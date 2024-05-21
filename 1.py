import docx
import MTK2
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_COLOR_INDEX

doc = docx.Document('C:\\Users\\Gdl\\Desktop\\ВКБ\\Сафарьян\\2\\2\\scrito.docx')


def run_get_spacing(run):
    rPr = run._r.get_or_add_rPr()
    spacings = rPr.xpath("./w:spacing")
    return spacings


def run_get_scale(run):
    rPr = run._r.get_or_add_rPr()
    scale = rPr.xpath("./w:w")
    return scale


def main():
    kod = ''
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            font_color = run.font.color.rgb
            font_size = run.font.size
            font_highlight_color = run.font.highlight_color
            font_scale = run_get_scale(run)
            font_spacing = run_get_spacing(run)

            if (font_color != RGBColor(0, 0, 0) or
                    font_size.pt != 15.0 or
                    font_highlight_color != WD_COLOR_INDEX.WHITE or
                    font_spacing or font_scale):
                for i in range(len(run.text)):
                    kod += '1'
            else:
                for i in range(len(run.text)):
                    kod += '0'


    #for paragraph in doc.paragraphs:
     #   for run in paragraph.runs:
     #       print(run.text)
    def decode_to_string(binary_string):
        
        unicode_chars = [binary_string[i:i + 16] for i in range(0, len(binary_string), 16)]
        decoded_message = ''.join([chr(int(char, 2)) for char in unicode_chars])
        return decoded_message
    print(kod)

    decoded_message = decode_to_string(kod)
    tttt = decoded_message.find('.') +1
    print("Декодированное сообщение:", decoded_message[:tttt])



if __name__ == '__main__':
    main()