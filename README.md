# Easily generates new components in a Vue.js project
Just execute the script with ```vue-generate.py <component name>``` to generate a new component, please write the component's name in PascalCase (the tag will be automatically converted to kebab-case).
(The script should be executed in the project's root folder) 
<br><br>

#### What it does:
1. It creates a new .vue file (named as you typed)
2. It adds the newly created component to the App.vue file
3. Now you're ready to use your new component!

###### P.S.: For faster use, for example, you could rename the script to something shorter, like vue-g.py.

# How to customize
If you want to change the generated component all you need to do is change the ```component_template``` string,

# Example
For example, you if launch the script as ```vue-generate.py HelloVue```, it will create a new file called ```HelloVue.vue``` and import it in the App.vue file. Now you can use the component as ```<HelloVue></HelloVue>``` or ```<hello-vue></hello-vue>```

## Contributors
[regi18](https://github.com/regi18/)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details<br><br>
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
