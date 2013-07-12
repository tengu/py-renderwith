# -*- coding: utf-8 -*-                                                                       
import unittest
import renderwith

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_render(self):
        
        expected="""
<html >
  <head >
   <style >
table, th, td                                                                                 
{                                                                                             
    border: 1px solid #ccc;                                                                   
}
   </style>
  </head>
  <body >
   <h1 >
some data
   </h1>
   <table >
    <tr >
     <th >
name
     </th>
     <th >
value
     </th>
    </tr>
    <tr >
     <td >
foo
     </td>
     <td >
42
     </td>
    </tr>
    <tr >
     <td >
bar
     </td>
     <td >
66
     </td>
    </tr>
   </table>
  </body>
</html>
""".strip()

        css="""                                                                                   
table, th, td                                                                                 
{                                                                                             
    border: 1px solid #ccc;                                                                   
}                                                                                             
        """.strip()

        data=dict(
            foo=42,
            bar=66,
            )

        r=renderwith.Render()

        with r.Html():
            with r.Head():
                with r.Style():
                    r.text(css)
            with r.Body():
                with r.H1():
                    r.text('some data')
                with r.Table():
                    with r.Tr():
                        for h in 'name value'.split():
                            with r.Th():
                                r.text(h)
                    for k,v in data.items():
                        with r.Tr():
                            with r.Td():
                                r.text(k)
                            with r.Td():
                                r.text(v)
        html='\n'.join(r.lines())
        print html
        self.assertEqual(html, expected)

if __name__=='__main__':

    unittest.main()
