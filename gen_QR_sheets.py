import qrcode
import os
from PIL import Image, ImageFont, ImageDraw

FONT = "C:/Windows/Fonts/arial.ttf"                 # font location for writing the QR code string
A4 = (1740, 2610)                                   # size of the paper to be used
PROJECT = 'test'                                    # project name
NUM_CODES = 30                                      # number of codes to be generated
INIT_INT = 0                                        # initial ID number


def qr_sheets(pages,
              size,
              label_template,
              font,
              qr_code_name,
              sheet_path,
              init_counter=0):

    for i in range(pages):

        # open blanksheet
        blank = Image.new(mode='RGB', size=size)
        draw = ImageDraw.Draw(blank)

        # for j in 18        18 tags per sheet
        for j in range(18):

            # create QR code
            code = (qr_code_name + "{0:0=4d}".format(init_counter))
            img = qrcode.make(code)

            # set LR position
            if j % 2 == 0:
                x = 0
            else:
                x = 870

            # set UD position
            y = int(j / 2) * 290

            # add QR code to blanksheet
            blank.paste(img, (x, y))

            # add template to blanksheet, if it exists
            if label_template:
                blank.paste(label_template, (x + 290, y))

            draw.text((x + 310, y + 240), 'ID: ' + code, (0, 0, 0), font=font)
            draw.line((x, y, blank.size[0], y), fill=(0, 0, 0))
            init_counter += 1

        draw.line((870, 0, 870, blank.size[1]), fill=(0, 0, 0))

        # save blanksheet
        blank.save(sheet_path + "/" + qr_code_name + "sheet" + str(i) + ".png")
        blank.close()


def main():

    project = PROJECT
    f_path = os.getcwd() + '/' + project
    sheet_path = f_path + '/sheets'
    if not os.path.isdir(sheet_path):
        os.mkdir(sheet_path)

    if not os.path.exists(f_path + "/label.png"):
        print("WARNING!!! no label.png exists in the %s directory. only QR codes will be printed" % project)
        template_img = None
    else:
        template_img = Image.open(f_path + "/label.png")

    num_codes = NUM_CODES
    first_id = INIT_INT

    pages = int(num_codes / 18) + 1
    font = ImageFont.truetype(FONT, size=20)

    qr_sheets(pages=pages,
              size=A4,
              label_template=template_img,
              font=font,
              qr_code_name=project,
              sheet_path=sheet_path,
              init_counter=first_id)


if __name__ == "__main__":
    main()
