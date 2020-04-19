#!/usr/bin/env python3

import PySimpleGUI as sg
import os
from biff import biff

sg.theme('LightGrey1')  # please make your creations colorful

current_folder=os.getcwd()
files_list=[]
out_str=''
width=80
options=[[sg.Spin(values=[100,150,200,300,400,600],initial_value=100,size=(7,1)),sg.Text('Exported images resolution (PPI)',size=(width-10,1))]]

col=[[sg.Text('no PDF files selected')]]

layout=[[sg.FilesBrowse('Select PDF file(s)',key='button_files',target='event_files',file_types=(('PDF Files', '*.pdf'),),initial_folder=current_folder,size=(width,1)),
         sg.Input(key='event_files', enable_events=True, visible=False)],
        [sg.Column(col,key='show_files',justification='left',element_justification='left')],
        [sg.FolderBrowse('Select Output folder',key='button_folder',target='output_folder',initial_folder=current_folder,size=(width,1))],
        [sg.Text('no Output Folder selected',key='output_folder',size=(width,1))],
        [sg.Text('> Output filenames will be [PDF_name].odt',size=(width,1))],
        [sg.Text('')],
        [sg.Frame('Options',options,size=(width,2))],
        [sg.Button(button_text="Extract Text",size=(int(width/2-3),1)),sg.Quit(size=(int(width/2-3),1))]]


window=sg.Window('Biff',layout)
while True:
    event,values=window.Read()
    if event in (None,'Quit'):
        break
    elif event in ('event_files'):
        col1=[[sg.Text('Two-Columns')]]
        col2=[[sg.Text('Filename')]]
        files_list+=values['event_files'].split(';')
        filename_list=[]
        
        for i,file in enumerate(files_list):
            filename_list.append(os.path.basename(file))
            col1.append([sg.Checkbox(text='',key=f'check_box_{i}')])
            col2.append([sg.Text(os.path.basename(file),justification='left')])
        
        current_folder=files_list[-1].replace(os.path.basename(files_list[-1]),'')

        options1=[[sg.Spin(values=[100,150,200,300,400,600],initial_value=100,size=(7,1),key='quality'),sg.Text('Exported images resolution (PPI)',size=(width-10,1))]]
        
        layout1=[[sg.FilesBrowse('Add PDF file(s)',key='button_files',target='event_files',file_types=(('PDF Files', '*.pdf'),),initial_folder=current_folder,size=(width,1)),
                 sg.Input(key='event_files', enable_events=True, visible=False)],
                [sg.Column(col1,key='show_check',element_justification='right'),sg.Column(col2,key='show_files')],
                [sg.FolderBrowse('Select Output folder',key='button_folder',target='output_folder',initial_folder=current_folder,size=(width,1))],
                [sg.Text('Current : '),sg.Text(current_folder,key='output_folder',size=(width-10,1))],
                [sg.Text('> Output filenames will be [PDF_name].odt',size=(width,1))],
                [sg.Text('')],
                [sg.Frame('Options',options1,size=(width,2))],
                [sg.Output(key="result",size=(width,5))],
                [sg.Button(button_text="Extract Text",size=(int(width/2-3),1)),sg.Quit(size=(int(width/2-3),1))]]

        window1 = sg.Window('Biff').Layout(layout1)
        window.Close()
        window = window1
        window.finalize()
        out_str+=f"{len(files_list)} PDF loaded.\n"
        
        window['result'](out_str)
        
    elif event in ("Extract Text"):
        
        for i,file in enumerate(files_list):
            filename=os.path.basename(file)
            input_folder=file.replace(filename,'')
            output_folder=current_folder
            two_col=values[f'check_box_{i}']
            img_quality=values['quality']
            
            out_str+=f"{biff.gui(filename,input_folder,output_folder,img_quality,two_col)}\n"
            out_str+='Done.\n'
            window['result'](out_str)
            
            window.Refresh
        print('')
        
        
window.close()