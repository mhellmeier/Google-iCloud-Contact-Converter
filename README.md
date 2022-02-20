Google iCloud Contact Converter
==========================
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

A simple Python script to convert Google Contacts vCard export into the correct Apple iCloud Contacts format.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
    - [Pre-Requirements](#pre-requirements)
    - [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)



## About The Project

**Current version**: 1.0

When moving from Google to Apple, e.g. when switching from an Android Phone to an iPhone, contacts may be transfered from Googles Contacts servers to Apples iCloud servers. When exporting and importing the data as vCard files, some information are missing or broken, like:

- Birthdays (with or without a year)
- Phone numbers in different categories (home, work, ...)
- Profile pictures
- etc.

This small Python script fixes all this issues by converting the Google Contacts export into a style that better suits the requirements from Apples iCloud Contacts app.


## Getting Started

### Pre-Requirements

To use the script, Python 3 is needed.

### Usage

More information and a detailed step-by-step guide is described in [this blog post](https://return2.net/google-to-apple-contacts-fix-import-export-problems-birthday-address-picture/).

1. Clone the repository and go into it
```sh
git clone https://github.com/mhellmeier/Google-iCloud-Contact-Converter.git
cd Google-iCloud-Contact-Converter
```
2. Export your contact data from [Google Contacts](https://contacts.google.com/) as vCard (`.vcf`) and put the file into the `data` folder
3. Open the main Python file (`google-icloud-contact-converter.py`) in the editor of your choice
4. Change the `AREA_CODE` to your default location
5. Change the `contacts_filename` to the name of your vCard file (from step 2)
4. Save the file and run it with
```sh
python3 google-icloud-contact-converter.py
```
5. A new file appears in the `data` folder (ends with "`_converted`")
6. Import the file into your [Apple iCloud Contacts](https://www.icloud.com/contacts/)
7. Done!


## Roadmap

All planned features, bugs and discussions can be found in the [open issues](https://github.com/mhellmeier/Google-iCloud-Contact-Converter/issues) section.


## Contributing

Feel free to fork the project, work in your personal branch and create a pull request or you simple interact in the [issue section](https://github.com/mhellmeier/Google-iCloud-Contact-Converter/issues).

**This is an open source project! Every contribution is greatly appreciated!**


## License

Distributed under the MIT License. See `LICENSE` for more information.


Original Project Link: [https://github.com/mhellmeier/Google-iCloud-Contact-Converter](https://github.com/mhellmeier/Google-iCloud-Contact-Converter)


[issues-shield]: https://img.shields.io/github/issues/mhellmeier/Google-iCloud-Contact-Converter.svg?style=flat-square
[issues-url]: https://github.com/mhellmeier/Google-iCloud-Contact-Converter/issues
[license-shield]: https://img.shields.io/github/license/mhellmeier/Google-iCloud-Contact-Converter.svg?style=flat-square
[license-url]: https://github.com/mhellmeier/Google-iCloud-Contact-Converter/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/malte-hellmeier-91a64a17b/