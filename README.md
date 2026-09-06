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

* **build_pdf.zsh**: Zshell script that executes pandoc with all the required library stuff. You may need to edit this based on your system's env variables and particular Latex package you have.

## Project Structure

    --ROOT : Index.md, build scripts, Latex config
        --assets
           --files : any support files needed
           --img : images. Duh.
        --guides : Markdown text files
        --output : Generated PDF
        --docs : HTML files
  
  
## Authoring Content

These docs are written in Markdown. There are also several bits specific to pandoc and Latex formatting.

    {height:} : specifies height of images
    H4 elements ("####") :  Configured in Latex to act 
       as headers, not Normal text

Note that these pandoc/Latex specific features may not render properly in your Markdown editor. Only make changes to pandoc or Latex configurations based on issues identified in the output, ***not*** your editor!

Index.md in the root and lists all chapter guides, which live in the "guides" folder. build_pdf.zsh consolidates each separate file in the guides folder. Edit the script to add any new Markdown files **IN ORDER**.

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
    
Link to that figure as desired:

    See [@fig:ID_TAG]
    