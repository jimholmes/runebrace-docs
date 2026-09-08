# README

## About
This project holds documentation for Runebrace, a 3D support, mesh manipulation, and printing slicer tool.

You can find current releases at [the Runebrace site](https://www.tarabella.it/Runebrace/index.html).

Support, as well as access to current beta releases, can be had on the Runebrace and Runebrace Slicer Beta channels on the [Artisan Guild Discord server](https://discord.gg/VTNVEksdje)

## Contributing

Contributions to the documentation are welcome. Feel free to submit a pull request. Contact [Jim directly](mailto:Jim@GuidePostSystems.com?subject=Runebrace%20Documentation) if you can't do that.

## Building the Docs

At the moment, HTML is the primary target, but as of the current commit, it's quite rough.

A consolidated PDF can also be generated. (See the build script.)

**Tools**

At the moment this is built locally on a Mac. The script and tools all have Windows and Linux variations, but you'll need to figure out how to get them running if you want to build on those platforms. If you do, please consider doing a PR with updated instructions, and include your build script as a separate file.

* **pandoc:** Converts Markdown to the output file, PDF at the moment. References the Latex header file (header.tex) for specific formatting. Install via Homebrew:

    `brew install pandoc`
    
* **pandoc crossref:** Provides cross-reference support. See below for examples.

    `brew install pandoc-crossref`
    
* **Mactex:** Provides PDF Latex support. Basictex might work, but is missing some key pieces which require separate installation. Install via Homebrew:

    `brew install --cask mactex`

* **build_nav.py** CALLED FROM BUILD_DOCS.ZSH. Python script to build nav.html based on headings in all the Markdown files. Invoke with "--docs" for setting BASE of the URL for deployment to GH Pages. Invoke with an empty to create for localhost deployment.

* **build_docs.zsh**: Zshell script that invokes build_nav.py, copies resource files to target, then executes pandoc with all the required library stuff. You may need to edit this based on your system's env variables and particular Latex package you have.

## Project Structure

    --ROOT : Index.md, build scripts, Latex config
        --assets
           --files : any support files needed
           --img : images. Duh.
        --css : css source files
        --guides : Markdown text files
        --output : Generated PDF
        --docs : output for web hosting. index.html is at this level
            --assets
               --img
               --files
            --css
            --guides: Converted HTML
        --scripts : zsh, py scripts, also ORDERED_FILE_LIST.txt
        --snippets : HTML 
  
  
## Authoring Content

These docs are written in Markdown. There are also several bits specific to pandoc and Latex formatting, for example:

    {height:} : specifies height of images
    H4 elements ("####") :  Configured in Latex to act 
       as headers, not Normal text

Note that these pandoc/Latex specific features may not render properly in your Markdown editor. Only make changes to pandoc or Latex configurations based on issues identified in the output, ***not*** your editor!

ORDERED_FILE_LIST holds a list of all Markdown files to be processed. *Exception:* index.md is handled separately due to its location.

Edit this file list to add new Markdown files. Files must be added in the order you want them appearing in the nav, TOC, etc.

### Examples

**Glossary**

To define a term in the Glossary:

    [Term]{#ID}
    : Definition...

IDs must be unique as they're all collapsed into one doc before rendering into the PDF.

Reference a term here the first time it's used in the docs. This will create a link to the definition:

    [Rim](#Rim)
    
**Figures and References**

Use standard Markdown image elements. Add an ID tag following the markup to create a reference, e.g.

    ![caption](image_path){#fig:ID_TAG}
    
ID tags are also required to generate "Figure <x>:" text as a caption.
    
Link to that figure as desired:

    See [@fig:ID_TAG]
    