from setuptools import setup

from geodatabase_tempfile import version

setup(name="geodatabase_tempfile",
	  version=version.__version__,
	  description="A library for managing temporary geodatabases and filenames in arcpy (ArcGIS) scripts",
	  long_description="""Implements a temporary geodatabase management system that wraps around arcpy.CreateScratchName
	  and arcpy.CreateUniqueName to manage the workspace that Unique/Scratch names are placed into, allowing you to focus
	  on just getting a name and not having to check where it's stored or whether your scratch database exists.
	  """,
	  packages=['geodatabase_tempfile', ],
	  install_requires=[],
	  author=version.__author__,
	  author_email="nrsantos@ucdavis.edu",
	  url='https://github.com/ucd-cws/geodatabase_tempfile',
	  )

