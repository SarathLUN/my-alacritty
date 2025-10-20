# Alacritty Configuration

This directory contains the configuration for the Alacritty terminal emulator.

## Directory Overview

This is a configuration directory for the Alacritty terminal emulator. It contains the main configuration file, a collection of themes, and some utility scripts for testing the terminal's rendering capabilities.

## Key Files

*   `alacritty.toml`: The main configuration file for Alacritty. This file imports a color scheme and sets various options for the terminal, such as the font, cursor style, and window behavior.
*   `alacritty.org`: A detailed, commented example of an Alacritty configuration file. It serves as a reference for all available configuration options.
*   `themes/`: This directory contains a large collection of color schemes for Alacritty.
*   `themes/README.md`: This file provides instructions on how to install and apply the themes included in the `themes` directory.
*   `themes/schemes.yaml`: A YAML file that defines the color palettes for many of the themes.
*   `smoke-test.sh`: A shell script used to display various text styles (bold, italic, underline) to test the terminal's rendering.
*   `test-fonts.sh`: A shell script for testing the rendering of Nerd Fonts, which include a large number of glyphs and icons.

## Usage

To customize the Alacritty terminal, you can edit the `alacritty.toml` file.

### Changing the Theme

To change the color scheme of the terminal, you can modify the `import` line in `alacritty.toml`. For example, to use the `catppuccin_mocha` theme, the line would be:

```toml
import = ["~/.config/alacritty/themes/themes/catppuccin_mocha.yaml"]
```

You can replace `catppuccin_mocha.yaml` with the filename of any other theme located in the `themes/themes/` directory.

### Changing the Font

The font can be changed by editing the `[font]` section in `alacritty.toml`. For example:

```toml
[font]
normal.family = "JetBrainsMono Nerd Font"
size = 16
```

### Testing the Configuration

You can use the provided shell scripts to test your configuration:

*   `./smoke-test.sh`: To test basic text rendering.
*   `./test-fonts.sh`: To test Nerd Font rendering.
