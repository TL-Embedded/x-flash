# x-flash

Script to help with in-field programming, targeting windows platforms using py2exe.

# Resources

The following resources are required, and not included in this repo:
 * `openocd/`: [Open OCD](https://github.com/openocd-org/openocd/releases/)
 * `drivers/stsw-link009`: [ST-Link Drivers](https://www.st.com/en/development-tools/stsw-link009.html)
 * `firmware/*`: the target firmware file (see config.json)

# Build
Run export.py. Distribute the following files
 * `dist/`
 * `firmware/`
 * `openocd/`
 * `drivers/` (optional)
 * `xflash.lnk`
 * `config.json`

