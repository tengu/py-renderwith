renderwith
==========

Quick'n'dirty html rendering from python. Becaus sometimes, you don't want to involve an 'engine' or language to spit out a little bit of html..

### Status

This is a proof of concenpt. This library generates ugly, invalid html. 
It's only good for quick'n'dirty personal reporting.  For externally visible documents, use one of the many production worthy templating engines.

### Pros

* No separate language to remember for control structures like loop and conditinal; it's all python.
* No template path and file management; render straight out of your python code.

### Example

         with r.Table():
             for k,v in data.items():
                 with r.Tr():
                     with r.Td():
                         r.text(k)
                     with r.Td():
                         r.text(v)
### todo:
* make an effort to comply..
* should build a tree, then render for better control.
