# icon_finder.py
Web-API for [iconfinder.com](https://www.iconfinder.com) an HTTP JSON API and allows you to programmatically access resources on the service, such as icons, icon sets, categories, styles, authors, etc

## Example
```python
import icon_finder
icon_finder = icon_finder.IconFinder(api_key="")
icon_details = icon_finder.get_icon_details(icon_id="")
print(icon_details)
```
