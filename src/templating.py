from jinja2 import Template

def apply_template(template, page):
    try:
        template_file = open(template, 'r')
    except:
        raise ValueError('Couldn\'t open %s' % template)
    tmpl = Template(template_file.read())
    
    try:
        page_date = load_page(page)
    except ValueError as e:
        raise ValueError('Error loading data for %s' % page)
    except Exception as e:
        raise RuntimeError('Error loading page data:\n\t%s' % str(e))

    return tmpl.render(page_data)

def load_page(page):
    pass
