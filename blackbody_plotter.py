import numpy as np
import astropy.io.fits as fits
from astropy import units as u
from PIL import Image
import arabic_reshaper
from bidi.algorithm import get_display
import json
from pathlib import Path
from glob import glob
from slugify import slugify
import astropy.constants as const
import argparse
# inspired by https://en.wikipedia.org/wiki/Planck%27s_law#/media/File:Black_body.svg

class MplColorHelper:

  def __init__(self, cmap_name, start_val, stop_val):
    self.cmap_name = cmap_name
    self.cmap = plt.get_cmap(cmap_name)
    self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
    self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

  def get_rgb(self, val):
    return self.scalarMap.to_rgba(val)

class SpectralLineSet:
  def __init__(self, name,lines,linestyle):
    self.name = name
    self.lines=lines #each line value can be either a single line value or two values (min and max) for a band
    self.linestyle=linestyle #a tuple containing linestyle parameters

def font_loader(possible_fonts):
    usable_fonts=[]
    #find any fonts in the font folder of package and load them
    packaged_fonts_path = Path(__file__).parent / 'fonts/*ttf'
    packaged_font_files=glob(str(packaged_fonts_path))
    for font_file in packaged_font_files:
        font_manager.fontManager.addfont(font_file)
    loaded_font_list=[f.name for f in font_manager.fontManager.ttflist]
    #loop over fonts for the required script and add any that are available to the list of fonts to pass to matplotlib
    for font in possible_fonts:
        if font in loaded_font_list:
            usable_fonts.append(font)
    if "Arial Unicode" in loaded_font_list:
        usable_fonts.append("Arial Unicode") #add Arial Unicode font as backup
    if "DejaVu Sans" in loaded_font_list:
        usable_fonts.append("DejaVu Sans") #add default matplotlib font as backup
    plt.rcParams['font.family']=usable_fonts #pass fonts to matplotlib
    
#Begin argument parsing
parser = argparse.ArgumentParser(description='Make spectrum plots of stars')

parser.add_argument('--lang', help='add language code')
parser.add_argument('--text-direction', help='add the text direction, ltr=left to right or rtl=right to left, default is ltr')
parser.add_argument('--plot_dir', help='add directory for output plots. Default is plots directory in this package.')
parser.add_argument('--translations_file', help='add the JSON file containing translations. Default is translations.json in this package.')
parser.add_argument('--output_format', help='add the output format for the plots. options: eps, jpg, jpeg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff. Default is png.',default='png')
parser.add_argument('--translate_filenames', help='If True output filenames will be in requested language. If False output filenames will be in English. Default is False',default=False)

args = parser.parse_args()

if not args.translations_file:
    translations_path = Path(__file__).parent / "./translations.json"
else:
    translations_path = Path(args.translations_file)
translations_file = open(translations_path)
translations_dicts = json.load(translations_file)
translations_file.close()

if not args.lang:
    need_language=True
else:
    if args.lang in translations_dicts.keys():
        language_code=args.lang
        need_language=False
    else:
        need_language=True
prompt_string="Available languages:"
for i0,key_tmp in enumerate(translations_dicts.keys()):
    if i0>0:
        prompt_string=prompt_string+', '
    prompt_string=prompt_string+key_tmp
prompt_string=prompt_string+'\nPlease enter a language code:'
while need_language:
    language_code=input(prompt_string)
    if language_code in  translations_dicts.keys():
        need_language=False

if not args.plot_dir:
    outfile_base = Path(__file__).parent / "./plots/"
else:
    outfile_base = Path(args.plot_dir)

#end argument parsing
#load translation file
text_list=translations_dicts[language_code]
possible_fonts=text_list['possible_fonts']

#important that arabic reshaper comes before bidi get_display
if language_code.startswith('ar'):
    text_list = {key:(arabic_reshaper.reshape(value) if type(value)==str else value) for key, value in text_list.items()}


text_list = {key:(get_display(value) if type(value)==str else value) for key, value in text_list.items()}

#check is cairo is required and load matplotlib
if text_list["matplotlib_cairo"]:
    import mplcairo
import matplotlib as mpl
if text_list["matplotlib_cairo"]:
    mpl.use("module://mplcairo.qt")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib import font_manager
from matplotlib import cm
    
text_list_en=translations_dicts['en']
font_loader(possible_fonts)

        
#setup plot definitions
lambda_min=10
lambda_max=3000
lambda_uv_min=10
lambda_vis_min=380
lambda_vis_max=750
lambda_red=650
lambda_blue=450


COL1 = MplColorHelper('rainbow',lambda_blue,lambda_red)
tmp_spec=[]
for i0 in range(lambda_vis_min,lambda_vis_max):
    if i0>lambda_red:
       tmp_list=list(COL1.get_rgb(lambda_red)) #if redder than lower limit of red light
            
    elif i0<lambda_blue:
        tmp_list=list(COL1.get_rgb(lambda_blue))  #if bluer than upper limit of blue light make it blue
    else:
        tmp_list=list(COL1.get_rgb(i0))
    tmp_list[3]=0.5
    tmp_list1=[255*x for x in tmp_list]
    tmp_spec.append(tmp_list1)
tmp_array=[]
for i0 in range(0,3000):
    tmp_array.append(tmp_spec)

wavelength=np.arange(lambda_min,lambda_max)
h = const.h.value
c = const.c.value
k_B = const.k_B.value
wavelength_tmp=1e-9*wavelength

teff_vec=[4000.0,6000.0,8000.0]


plt.figure()
plt.rcParams['figure.figsize']= 15,8
plt.rcParams.update({'font.size': 12})
mpl.rcParams['axes.linewidth'] =1.0
#lines = ['--','-.',':']
offset=1.1
max_intensity=-1.0
for index,Teff in enumerate(teff_vec):
    specific_intensity=np.pi*1.0e-12*(2.0*h*c**2/wavelength_tmp**5)*1.0/(np.exp(h*c/(wavelength_tmp*k_B*Teff))-1.0)
    max_intensity_tmp=max(specific_intensity)
    max_intensity=max([max_intensity,max_intensity_tmp])
fig,ax=plt.subplots(1,1)
tmp_array1=np.array(tmp_array).astype('uint8')
img_tmp = Image.fromarray(tmp_array1, mode='RGBA')
ax.imshow(img_tmp,extent=[lambda_vis_min,lambda_vis_max,0,offset*max_intensity], aspect='auto')
ax.tick_params(axis='both', which='major', labelsize=14)
for index,Teff in enumerate(teff_vec):
    specific_intensity=np.pi*1.0e-12*(2.0*h*c**2/wavelength_tmp**5)*1.0/(np.exp(h*c/(wavelength_tmp*k_B*Teff))-1.0)
    max_intensity_tmp=max(specific_intensity)
    wavelength_at_max=wavelength[specific_intensity.argmax()]
    ax.text(wavelength_at_max,max_intensity_tmp+0.02*max_intensity,text_list_en['teff'+str(index+1)],ha='center',fontsize=14)
    ax.plot(wavelength,specific_intensity,color='k')
ax.text(0.5*(lambda_vis_min+lambda_vis_max),1.09*max_intensity,text_list['vis_text'],ha='center',va='top',fontsize=14)
ax.text(0.5*(lambda_vis_min+lambda_uv_min),1.09*max_intensity,text_list['uv_text'],ha='center',va='top',fontsize=14)
ax.text(0.5*(lambda_max+lambda_vis_max),1.09*max_intensity,text_list['ir_text'],ha='center',va='top',fontsize=14)
ax.set_ylim(0,offset*max_intensity)
ax.set_xlim(lambda_min,lambda_max)
ax.set_ylabel(text_list['yaxis_text'],fontsize=20)
ax.set_xlabel(text_list['xaxis_text'],fontsize=20)
ax.set_title(text_list['title_text'],fontsize=26)
if args.translate_filenames:
    filename_tmp=slugify(text_list['title_text'])+'_'+language_code
    filename_tmp_uv_cat=slugify(text_list['title_text_uv_cat'])+'_'+language_code
else:
    filename_tmp=slugify(text_list_en['title_text'])+'_'+language_code
    filename_tmp_uv_cat=slugify(text_list_en['title_text_uv_cat'])+'_'+language_code
    
print("Saving: ",text_list_en['title_text']+'\nTo: '+str(outfile_base.joinpath(filename_tmp+'.'+str.lower(args.output_format))))
plt.savefig(outfile_base.joinpath(filename_tmp+'.'+str.lower(args.output_format)))
specific_intensity_uv_cat=np.pi*1.0e-12*(2.0*k_B*c*8000.0/wavelength_tmp**4)
ax.plot(wavelength,specific_intensity_uv_cat,color='k',linestyle=':')
label_index=int((lambda_max-lambda_min)/3)
ax.text(wavelength[label_index],1.02*specific_intensity_uv_cat[label_index],text_list['text_uv_cat'],ha='left',fontsize=14)
print("Saving: ",text_list_en['title_text_uv_cat']+'\nTo: '+str(outfile_base.joinpath(filename_tmp_uv_cat+'.'+str.lower(args.output_format))))
plt.savefig(outfile_base.joinpath(filename_tmp_uv_cat+'.'+str.lower(args.output_format)))
plt.close()
