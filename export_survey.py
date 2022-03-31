import arcgis
from arcgis.gis import GIS
import os, re, csv

#https://developers.arcgis.com/survey123/guide/export-survey-data-with-attachments/

#connection to ArcGIS Account
portalURL = "https://www.arcgis.com"
username = "hluening_wwu"
password = "emHD2YKl3zs1"
survey_item_id = "6edab402fba746baa797d4b2cdeb45e5"
save_path = r"C:\Users\he-lu\OneDrive - Universität Münster\Code\LeezGo"
keep_org_item = False
store_csv_w_attachments = False

#connection to ArcGIS organization
gis = GIS(portalURL, username, password)
survey_by_id = gis.content.get(survey_item_id)

#download survey's feature service
rel_fs = survey_by_id.related_items('Survey2Service','forward')[0]
item_excel = rel_fs.export(title=survey_by_id.title, export_format='Excel')
item_excel.download(save_path=save_path)
if not bool(keep_org_item):
    item_excel.delete(force=True)


layers = rel_fs.layers + rel_fs.tables
for i in layers:
    if i.properties.hasAttachments == True:
        feature_layer_folder = os.path.join(save_path, '{}_attachments'.format(re.sub(r'[^A-Za-z0-9]+', '', i.properties.name)))
        os.mkdir(feature_layer_folder)
        if bool(store_csv_w_attachments):
            path = os.path.join(feature_layer_folder, "{}_attachments.csv".format(i.properties.name))
        elif not bool(store_csv_w_attachments):
            path = os.path.join(save_path, "{}_attachments.csv".format(i.properties.name))
        csv_fields = ['Parent objectId', 'Attachment path']
        with open(path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(csv_fields)
            
            feature_object_ids = i.query(where="1=1", return_ids_only=True, order_by_fields='objectid ASC')
            for j in range(len(feature_object_ids['objectIds'])):
                current_oid = feature_object_ids['objectIds'][j]
                current_oid_attachments = i.attachments.get_list(oid=current_oid)
            
                if len(current_oid_attachments) > 0:
                    for k in range(len(current_oid_attachments)):
                        attachment_id = current_oid_attachments[k]['id']
                        current_attachment_path = i.attachments.download(oid=current_oid, attachment_id=attachment_id, save_path=feature_layer_folder)
                        csvwriter.writerow([current_oid, os.path.join('{}_attachments'.format(re.sub(r'[^A-Za-z0-9]+', '', i.properties.name)), os.path.split(current_attachment_path[0])[1])])