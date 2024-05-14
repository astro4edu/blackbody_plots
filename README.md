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
  --unicode_font UNICODE_FONT
                        If you are using mplcairo as a backend then use this argument. See "fonts" later in this document
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
### Simplified Chinese
Niall Deacon

<!-- end-translation-credits -->

## Adding your own translation
You can add your own translations by downloading this repository and editing the translations.json file. Each language starts with a [language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) followed by translations of each text element. We have included a placeholder `zz` language code that you can edit (or copy and edit if you want to add more than one language). For example if you were to translate the terms into Brazilian Portuguese you would edit:
```
 "zz": {
    "translation_approval_level": "N",
    "translation_credit": null,
    "matplotlib_cairo": false,
    "possible_fonts": [
      "Noto Sans",
      "Arial"
    ],
    "title_text": "Blackbody Radiation",
    "title_text_uv_cat": "Blackbody Radiation ultraviolet catastrophe",
    "xaxis_text": "Wavelength (nm)",
    "yaxis_text": "Radiation emitted (kW/m$^2$/nm)",
    "uv_text": "ultraviolet",
    "vis_text": "visible light",
    "ir_text": "infrared",
    "teff1": "4000 K",
    "teff2": "6000 K",
    "teff3": "8000 K",
    "text_uv_cat": "Classical theory - 8000 K"
  }
```
And instead have:
```
"pt-br": {
    "translation_approval_level": "N",
    "translation_credit": null,
    "matplotlib_cairo": false,
    "possible_fonts": [
      "Noto Sans",
      "Arial"
    ],
    "title_text": "Radiação de corpo negro",
    "title_text_uv_cat": "Radiação de corpo negro catástrofe do ultravioleta",
    "xaxis_text": "Comprimento de onda (nm)",
    "yaxis_text": "Radiação emitida (kW/m$^2$/nm)",
    "uv_text": "ultravioleta",
    "vis_text": "luz visível",
    "ir_text": "infravermelho",
    "teff1": "4000 K",
    "teff2": "6000 K",
    "teff3": "8000 K",
    "text_uv_cat": "Teoria clássica - 8000 K"
}
```

Then just run:
```python3 blackbody_plotter.py --lang=zz```
With `zz` replaced by your language code.

<!-- start-diagram-links -->

## Diagram Links
 Below are links to the diagrams produced by this code. You can also find the diagram captions and any translations of these captions in the links.
 <ul>
<li><a href="http://astro4edu.org/resources/diagram/JI31N7441y90/">a diagram</a></li>
</ul>

<!-- end-diagram-links -->


## Fonts
The built-in fonts for matplotlib often struggle with non-Latin characters. The code is set up to try to load commonly used fonts for the writing system it is producing the plots for. If you want to load a font that is already installed on your system then you can tell the code to use that font by adding it to the start of the list in the `possible_fonts` list in `translations.json`. If you are struggling to get a particular writing system to work with this code then you can download the font you want to use and copy the `.ttf` file to the `fonts` folder of this repository. The code will then automatically load that font. The Google <a href="https://fonts.google.com/noto">Noto Fonts</a> project provides fonts in a wide range of writing systems. For some writing systems (mostly scripts used in South Asia such as Devanagari or Bengali) we recommend you use the <a href="https://pypi.org/project/mplcairo/">mplcairo matplotlib backend</a>. Once you have installed mplcairo, change "matplotlib_cairo" from false to true (lowercase, no quotemarks). We do not include mplcairo in the requirements.txt file as it is a little complex to install and only required by some users. Note the diagrams used here have an additional problem of having superscript letters in them. In the standard backend for matplot lib one can just include LaTeX maths notation. Unfortunately doing this seems to cause mplcairo to fallback to the standard matplotlib backend, causing issues with some text rendering. The workaround is to use the unicode superscript 2 character, copy a unicode font that covers the whole unicode basic multilingual plane into the fonts directory and then name the font with the ```--unicode_font=``` option. The best font to use here would be Arial Unicode MS but that is not available on all systems.

## Important Caveats

The color representation is a linear colour spectrum from 450-650nm. Bluer than 450nm is coloured blue, even though the human eye sees very little bluer than 400nm. Redder than 650nm is coloured red even thought the human eye has very little redder than 750nm.

For languages other than English, please check the translation approval level in the translations.json file. If approval level is marked as 'N' then the translation has not been reviewed, translations marked 'Y' have been approved by a reviewer in our review system.
