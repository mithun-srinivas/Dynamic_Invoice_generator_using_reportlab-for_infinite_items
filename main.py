from reportlab.pdfgen import canvas

item = ['one','two','three','four','five','imp','1','2','3','4','5','2','1','2','3','4','5','2','1','2','3','4','5','2']
rate = ['1','2','3','4','5','100','1','2','3','4','5','2','1','2','3','4','5','2','1','2','3','4','5','2']
quantity = ['1','2','3','4','5','2','1','2','3','4','5','2','1','2','3','4','5','2','1','2','3','4','5','2']
total = [1,2,3,4,5,200,1,2,3,4,5,200,1,2,3,4,5,200,1,2,3,4,5,200]
leng=24
invoice_number = '1'
name = 'mithun'
phone_number = '6366256689'
date = '27/02/2002'
adress = 'line1'
state = 'karnataka'
zip = 563131

def create_pdf(leng,item,rate,quantity,total,invoice_number,name,phone_number,date,adress,state,zip):
    pdf_file = 'multipage1.pdf'
    c = canvas.Canvas(pdf_file, pagesize=(700, 750));

    leng
    page_limit = 15
    item_number = 1
    list_index = 0
    x = 10
    y = 400
    item_x = 55
    rate_x = 480
    quantity_x = 530
    total_x = 600
    item 
    rate
    quantity
    total
    grandtotal = 0
    initial_check = 0
    while leng > initial_check:
        while item_number <= leng:
            c.line(150, 720, 690, 720)
            c.drawString(450, 730, 'MIILLIION PAGES')

            c.drawImage('logo.png', 30, 670, 70, 70)

            c.line(10, 660, 690, 660)
            c.drawString(450, 705, '#21/A, 5th Main road 3rd phase')
            c.drawString(450, 685, ',Peenya industrial area, Bengaluru-560058')
            c.drawString(450, 665, 'GSTIN : 07AABCS1429B1Z')

            c.drawString(300, 645, 'INVOICE')

            c.rect(10, 550, 680, 90)
            c.drawString(50, 620, 'Invoice Number :')
            c.drawString(50, 600, 'Customer Name :')
            c.drawString(50, 580, 'Phone Number :')
            c.drawString(50, 560, 'Date :')

            invoice_number
            name
            phone_number
            date

            c.drawString(180, 620, invoice_number)
            c.drawString(180, 600, name)
            c.drawString(180, 580, phone_number)
            c.drawString(180, 560, date)

            c.rect(10, 440, 680, 100)

            c.drawString(50, 525, 'Billing Adress :')
            adress
            state
            zip
            country = 'India'
            c.drawString(180, 525, adress)
            c.drawString(180, 510, state)
            c.drawString(180, 495, country)
            c.drawString(220, 495, str(zip))

            c.drawString(50, 480, 'Shipping Adress :')
            c.drawString(180, 480, adress)
            c.drawString(180, 465, state)
            c.drawString(180, 450, country)
            c.drawString(220, 450, str(zip))

            c.rect(10, 10, 680, 60)
            c.line(320, 10, 320, 70)
            c.drawString(20, 50, 'We declare that above mentioned information is true.')
            c.drawString(50, 35, '(This is system generated invoive) ')
            c.drawString(450, 50, 'Authorised Signature :')
            c.drawString(450, 30, 'Mithun.S')

            c.drawString(x, 420, 'Si. no')
            c.drawString(item_x, 420, 'Item Name')
            c.drawString(rate_x, 420, 'Rate')
            c.drawString(quantity_x, 420, 'Quantity')
            c.drawString(total_x, 420, 'Total')
            c.drawString(510, 80, 'Grand Total :')
            while item_number <= page_limit:
                if (item_number <= leng):
                    c.setFontSize(8)
                    c.drawString(x, y, str(item_number))
                    c.drawString(item_x, y, item[list_index])
                    c.drawString(rate_x, y, rate[list_index])
                    c.drawString(quantity_x, y, quantity[list_index])
                    c.drawString(total_x, y, str(total[list_index]))
                    y = y - 20
                    grandtotal = grandtotal + total[list_index]
                item_number = item_number + 1
                list_index = list_index + 1
            page_limit = page_limit + 15
            c.drawString(590, 80, str(grandtotal))
            y = 400
            c.showPage()

        initial_check = initial_check +15



    c.save()

create_pdf(leng,item,rate,quantity,total,invoice_number,name,phone_number,date,adress,state,zip)
