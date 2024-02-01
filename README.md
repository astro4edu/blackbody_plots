## What this repository does	
This repository creates a series of plots of stellar spectra in multiple languages. 

## How to create plots using this repository
The command to run code from this repository is:
`python3 blackbody_plotter.py`
The following command line options are available:
```-h, --help            show this help message and exit
  --lang LANG           add language code
  --plot_dir PLOT_DIR   add directory for output plots. Default is plots directory in this repository.
  --translations_file TRANSLATIONS_FILE
                        add your own JSON file containing translations. Default is translations.json in this repository.
  --output_format OUTPUT_FORMAT
                        add the output format for the plots. options: eps, jpg, jpeg, pdf, pgf, png, ps, raw, rgba,
                        svg, svgz, tif, tiff. Default is png.
  --translate_filenames TRANSLATE_FILENAMES
                        If True output filenames will be in requested language. If False output filenames will be in
                        English. Default is False
```
Example usage, for English, using untranslated filenames, the default translation file, pdf output format and output directory "/home/user/plots/", one would use the command:
```python3 blackbody_plotter.py --lang=en --output_format=pdf --plot_dir=/home/user/plots/ ```
The code creates one plot for each of the seven spectral types (showing both a line of wavelength vs flux and a band plot showing light and dark patches on the spectrum) and two comparison plots showing all seven spectra (one with a line plot, one with a band plot).

## License
The code released is available under an MIT license and should be credited to IAU OAE/Niall Deacon. The plots in the plots directory and the translations in the translations directory are published under a <a href="https://creativecommons.org/licenses/by/4.0/deed.en">CC-BY-4.0 license</a>.

## Plot Credits
Please credit all plots created by this code to IAU OAE/Niall Deacon. For languages other than English, please also credit the translators listed below. Some of the characteristics of the plots were inspired by the following <a href="https://en.wikipedia.org/wiki/Planck%27s_law#/media/File:Black_body.svg">plot from Wikipedia</a>.
<!-- start-translation-credits -->

## Translation credits
### German
Niall Deacon

<!-- end-translation-credits -->

## Adding your own translation
You can add your own translations by downloading this repository and editing the translations.json file. Each language starts with a [language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) followed by translations of each text element. We have included a placeholder `zz` language code that you can edit (or copy and edit if you want to add more than one language). For example if you were to translate the terms into Brazilian Portuguese you would edit:
```
 "zz":{
	"translation_approval_level":"N",
	"Translation Credit":null,
	"matplotlib_cairo": false,
	"possible_fonts": [
     		 "Noto Sans",
     		 "Arial"
		],
        "xaxis_text":"Wavelength (nanometers)",
        "yaxis_text":"Flux",
        "spectral_features_title":"Important spectral features",
        "balmer_text":"Hydrogen atoms",
        "helium_atoms_text":"Helium atoms",
        "helium_ions_text":"Helium ions",
        "calcium_atoms_text":"Calcium atoms",
        "calcium_ions_text":"Calcium ions",
        "sodium_atoms_text":"Sodium atoms",
        "titanium_oxide_text":"Titanium Oxide",
        "title0":"Spectrum of an O-type star",
        "title1":"Spectrum of a B-type star",
        "title2":"Spectrum of an A-type star",
        "title3":"Spectrum of an F-type star",
        "title4":"Spectrum of a G-type star",
        "title5":"Spectrum of a K-type star",
        "title6":"Spectrum of an M-type star",
        "spectrum_title0":"O-type star",
        "spectrum_title1":"B-type star",
        "spectrum_title2":"A-type star",
        "spectrum_title3":"F-type star",
        "spectrum_title4":"G-type star",
        "spectrum_title5":"K-type star",
        "spectrum_title6":"M-type star",
        "bands_title":"Stellar Spectra",
        "lambda_lower":"365 nm",
        "lambda_upper":"900 nm",
	"bands_filename":"spectra bands",
	"lines_filename":"spectra lines"
        }
```
And instead have:
```
"pt-br": {
	"translation_approval_level": "N",
	"Translation Credit":"Translator: Eduardo Penteado",
	"matplotlib_cairo": false,
	"possible_fonts": [
     		 "Noto Sans",
     		 "Arial"
		],
	"xaxis_text": "comprimento de Onda (nanômetros)",
	"yaxis_text": "fluxo",
	"spectral_features_title": "características espectrais importantes",
	"balmer_text": "átomos de Hidrogênio",
	"helium_atoms_text": "átomos de Hélio",
	"helium_ions_text": "íons de Hélio",
	"calcium_atoms_text": "Átomos de Cálcio",
	"calcium_ions_text": "íons de Cálcio",
	"sodium_atoms_text": "átomos de Sódio",
	"titanium_oxide_text": "óxido de Titânio",
	"title0": "Espectro de uma estrela do tipo O",
	"title1": "Espectro de uma estrela do tipo B",
	"title2": "Espectro de uma estrela do tipo A",
	"title3": "Espectro de uma estrela do tipo F",
	"title4": "Espectro de uma estrela do tipo G",
	"title5": "Espectro de uma estrela do tipo K",
	"title6": "Espectro de uma estrela do tipo M",
	"spectrum_title0": "estrela do tipo O",
	"spectrum_title1": "estrela do tipo B",
	"spectrum_title2": "estrela do tipo A",
	"spectrum_title3": "estrela do tipo F",
	"spectrum_title4": "estrela do tipo G",
	"spectrum_title5": "estrela do tipo K",
	"spectrum_title6": "estrela do tipo M",
	"bands_title": "Espectros Estelares",
	"lambda_lower": "365 nm",
	"lambda_upper": "900 nm",
	"bands_filename": "bandas_espectrais",
	"lines_filename": "linhas_espectrais" },
```

Then just run:
```python3 blackbody_plot.py --lang=zz```
With `zz` replaced by your language code.

<!-- start-diagram-links -->

## Diagram Links
 Below are links to the diagrams produced by this code. You can also find the diagram captions and any translations of these captions in the links.
 <ul>
<li><a href="http://astro4edu.org/resources/diagram/JI31N7441y90/">a diagram</a></li>
</ul>

<!-- end-diagram-links -->


## Fonts
The built-in fonts for matplotlib often struggle with non-Latin characters. The code is set up to try to load commonly used fonts for the writing system it is producing the plots for. If you want to load a font that is already installed on your system then you can tell the code to use that font by adding it to the start of the list in the `possible_fonts` list in `translations.json`. If you are struggling to get a particular writing system to work with this code then you can download the font you want to use and copy the `.ttf` file to the `fonts` folder of this repository. The code will then automatically load that font. The Google <a href="https://fonts.google.com/noto">Noto Fonts</a> project provides fonts in a wide range of writing systems. For some writing systems (mostly scripts used in South Asia such as Devanagari or Bengali) we recommend you use the <a href="https://pypi.org/project/mplcairo/">mplcairo matplotlib backend</a>. Once you have installed mplcairo, change "matplotlib_cairo" from false to true (lowercase, no quotemarks). We do not include mplcairo in the requirements.txt file as it is a little complex to install and only required by some users.

## Important Caveats

The color representation is a linear colour spectrum from 450-650nm. Bluer than 450nm is coloured blue, even though the human eye sees very little bluer than 400nm. Redder than 650nm is coloured red even thought the human eye has very little redder than 750nm.

For languages other than English, please check the translation approval level in the translations.json file. If approval level is marked as 'N' then the translation has not been reviewed, translations marked 'Y' have been approved by a reviewer in our review system.
