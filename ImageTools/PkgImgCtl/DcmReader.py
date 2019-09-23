import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages")
import dicom
class DcmReader:
    def __init__(self):
        return
    
    def LoadFromFile(self, FilePath):
        ds=dicom.read_file(FilePath) 
        pixel_bytes = ds.PixelData
        #ds = pydicom.read_file("rtplan.dcm") # (rtplan.dcm is in the testfiles directory)
        return pixel_bytes
