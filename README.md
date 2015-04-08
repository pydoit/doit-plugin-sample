A sample command plugin for [doit](http://pydoit.org).


## setuptools integration

If you install this module using setuptools/pip,
`doit` will auto-load the plugin on its execution.

```
pip install git+https://github.com/pydoit/doit-plugin-sample.git
```

Note that in the plugin `setup.py` the entry-point group should
be `doit.` followed by the plugin category name, in this case `COMMAND`.

```
      entry_points = {
          'doit.COMMAND': [
              'plug_sample = doit_sample_cmd:SampleCmd'
          ]
      },
```

## local plugins

It is also possible to just put this module anywhere in your `PYTHONPATH`
and enable it by adding the following lines into you `doit.cfg` file:

```
[COMMAND]
plug_sample = doit_sample_cmd:SampleCmd
```
