from jinja2 import Template
janapith_data = [{'year': 1965, 'name': 'G. Sankara Kurup', 'language': 'Malayalam'},
                  {'year': 1966, 'name': 'Tarasankar Bandopadhyay', 'language': 'Bengali'},
                  {'year': 1967, 'name': 'Kuppali Venkatappagowda Puttappa', 'language': 'Kannada'},
                  {'year': 1968, 'name': 'Sumitranandan Pant', 'language': 'Hindi'},]





def main():
    template_file=open('jananpith.html')
    TEMPLATE=Template(template_file.read())
    template_file.close()

    template=Template(TEMPLATE)
    cotent=template.render(janapith_data=janapith_data)


    template=Template(template_file.read())
    print(template.render(janapith_data=janapith_data))
if __name__ == "__main__":
    main()



