import sys
import os
import shutil  #copy files

ARCPY_PATH = r"C:/Program Files (x86)/ArcGIS\Desktop10.5/arcpy"
sys.path.append(ARCPY_PATH)
import arcpy

#from arcpy import env


def process_gdb(gdbpathname, filterprefix):#, outfolder, outname):
    print("\n\nBuilding GeoDatabase: " + gdbpathname)
    arcpy.env.workspace=gdbpathname
    try:
        #create output gdb
        #http://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-file-gdb.htm
        #arcpy.CreateFileGDB_management(outfolder, outname)

        datasets = arcpy.ListDatasets(feature_type='feature')
        for ds in datasets:
            print("\tProcessing DataSet: " + ds)
            fcs = arcpy.ListFeatureClasses(None, None, ds)
            for fc in fcs:
                # get the FIPS Code

                if(filterprefix != None and not(fc.lower().startswith(filterprefix))):
                    continue

                fips = ""
                with arcpy.da.SearchCursor(fc, ['FIPS']) as cursor:
                    for row in cursor:
                        fips = row[0]
                        break
                        
                outputFeatureClass = fc + "_" + fips
                print('\t\tFeature Class: {} -> {}'.format(fc, outputFeatureClass))

                arcpy.CopyFeatures_management(fc, outputFeatureClass)
                arcpy.Delete_management(fc)
        
            arcpy.Delete_management(ds)

    except Exception:
        print(Exception.message)

print("Looking for Parcel gdbs in " + os.path.join(os.getcwd(), 'input'))

gdbs = []
dirs = os.walk(os.path.join(os.getcwd(), "input"))
for dir in dirs:
    if dir[0].endswith(".gdb") : # skip output folder
        gdbs.append(dir[0])

print('\nFound these Geodatabases to wrangle parcels in:\n{}\n'.format(gdbs))

processed_count = 0

for gdb in gdbs:
    # name output file and delete if it exists
    directory = os.path.join(os.getcwd(),'output')
    if not os.path.exists(directory):
        os.makedirs(directory)

    outfilePoints = os.path.join(os.getcwd(),'output',os.path.splitext(os.path.basename(gdb))[0]+'_Parcels_Points.gdb')
    outfilePolys =  os.path.join(os.getcwd(),'output',os.path.splitext(os.path.basename(gdb))[0]+'_Parcels_Polys.gdb')

    try:
        shutil.copytree(gdb, outfilePoints)
        process_gdb(outfilePoints, 'propertypoints')

        shutil.copytree(gdb, outfilePolys)
        process_gdb(outfilePolys, 'parcels')

       # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

    processed_count = processed_count +1
    print('Processed {} of {} gdbs'.format(processed_count, len(gdbs)))

print("### Done ###")
