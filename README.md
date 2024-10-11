# icon_finder.js
Web-API for [iconfinder.com](https://www.iconfinder.com) an HTTP JSON API and allows you to programmatically access resources on the service, such as icons, icon sets, categories, styles, authors, etc

## Example
```JavaScript
async function main() {
	const { IconFinder } = require("./icon_finder.js")
	const iconFinder = new IconFinder("apiKey")
	const categories = await iconFinder.getAllCategories()
	console.log(categories)
}

main()
```
