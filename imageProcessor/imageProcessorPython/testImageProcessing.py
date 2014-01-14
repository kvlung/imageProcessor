# !/usr/bin/python

from ImageProcessor import ImageProcessor
from Image import Image

class testImageProcessing:
    def __init__ ( self ):
        self.x = 5
        self.is_setup = 0
        self.image = Image()
        self.imageProcessor = ImageProcessor( self.image )
        if not self.is_setup: 
            self.setup()

    def setup( self ):
        self.is_setup = 1
   
    def teardown( self ):
        self.is_setup = 0

    def test_nose( self ):
        tolerance = 1e-12
        result = 5
        assert abs( result - self.x ) < tolerance

class testImage:
    def __init__( self ):
        self.image = Image()
        self.is_setup = 0
        if not self.is_setup:
            self.setup()

    def setup( self ):
        self.is_setup = 1

    def teardown( self ):
        self.is_setup = 0

    def test_sizeX( self ):
        tolerance = 1e-12
        result = 300
        assert abs( result - self.image.sizeX ) < tolerance
