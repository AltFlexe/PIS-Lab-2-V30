from pathlib import Path
from lxml import html, etree
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


class PageTests(SimpleTestCase):
    def test_home_uses_styled_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "static_handler.html")
        self.assertContains(response, '/static/index.css')
        self.assertContains(response, '/static/book.svg')

    def test_response_types_have_same_text(self):
        plain = self.client.get("/hello/plain/")
        default = self.client.get("/hello/")
        self.assertEqual(plain.status_code, 200)
        self.assertEqual(default.status_code, 200)
        self.assertEqual(plain.content, "Привет, Мир!".encode())
        self.assertEqual(plain.content, default.content)
        self.assertEqual(plain["Content-Type"], "text/plain; charset=utf-8")
        self.assertEqual(default["Content-Type"], "text/html; charset=utf-8")

    def test_template_has_seven_rows_six_columns_and_headers(self):
        for address in ("/", "/template/"):
            with self.subTest(address=address):
                tree = html.fromstring(self.client.get(address).content)
                self.assertEqual(len(tree.xpath('//table/thead/tr/th')), 6)
                rows = tree.xpath('//table/tbody/tr')
                self.assertEqual(len(rows), 7)
                self.assertTrue(all(len(row.xpath('./td')) == 6 for row in rows))
                self.assertEqual(rows[-1][-1].text, "Свободно")

    def test_list_headings_are_h4(self):
        for address in ("/", "/template/"):
            tree = html.fromstring(self.client.get(address).content)
            self.assertEqual(len(tree.xpath('//h4')), 2)
            self.assertEqual(len(tree.xpath('//ul/li')), 4)
            self.assertEqual(len(tree.xpath('//ol/li')), 4)
            self.assertEqual(tree.xpath('//ul/preceding-sibling::*[1]')[0].tag, 'h4')
            self.assertEqual(tree.xpath('//ol/preceding-sibling::*[1]')[0].tag, 'h4')
            self.assertFalse(tree.xpath('//h4/ul|//h4/ol'))

    def test_index_is_retained_without_external_styles(self):
        response = self.client.get('/template/')
        self.assertTemplateUsed(response, 'index.html')
        tree = html.fromstring(response.content)
        self.assertFalse(tree.xpath('//link[@rel="stylesheet"]'))
        self.assertFalse(tree.xpath('//img'))
        self.assertIn('border: 1px solid', tree.xpath('//style/text()')[0])

    def test_static_files_resolve_and_svg_is_well_formed(self):
        css = finders.find('index.css')
        picture = finders.find('book.svg')
        self.assertIsNotNone(css)
        self.assertIsNotNone(picture)
        self.assertTrue(Path(css).is_file())
        self.assertTrue(etree.parse(str(picture)).getroot().tag.endswith('svg'))

    def test_template_contents_stay_equal_except_styling_and_picture(self):
        def contents(address):
            tree = html.fromstring(self.client.get(address).content)
            return [(node.tag, (node.text or '').strip())
                    for node in tree.xpath('//body//*') if node.tag != 'img']
        self.assertEqual(contents('/'), contents('/template/'))

    def test_named_routes_and_missing_page(self):
        expected = {'home':'/', 'hello':'/hello/', 'hello_plain':'/hello/plain/',
                    'template_page':'/template/'}
        for name, address in expected.items():
            self.assertEqual(reverse(name), address)
        self.assertEqual(self.client.get('/missing/').status_code, 404)
