import requests

class IconFinder:
	def __init__(self, api_key: str) -> None:
		self.api = "https://api.iconfinder.com/v4"
		self.api_key = api_key
		self.headers = {
			"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
			"authorization": f"Bearer {self.api_key}"
		}
		
	def search_icons(
			self,
			query: str,
			count: int = 1,
			offset: int = 0,
			premium: str = None,
			vector: str = None,
			license: str = None,
			category: str = None,
			style: str = None,
			is_explicit: bool = None) -> dict:
		"""
		Get the list of strings that contains random names
		Parameters:
			query: (str): string <the search query>
			count: (int): integer <int32> -> <number of icons to include in the result>
			offset: (int): integer <int32> -> <result offset. starts from 0, resulting in the first count icons being returned>
			premium: (str): string <all, empty - include all icons> <0, false - only include nonpremium icons> <1, true - only include premium icons>
			vector: (str): string <all, empty - include all icons> <0, false - only include raster icons> <1, true - only include vector icons>
			license: (str): string <none, empty - include all icons> <commercial - only include icons that can be used commercially> <commercial-nonattribution - only include icons that be used commercially without any attribution requirements>
			category: (str): string <category identifier>
			style: (str): string <style identifier>
			is_explicit: (bool): boolean <false - exclude all explicit content> <true - return only explicit content>
		Returns: 
			dict: list of icons by search query
		"""
		url = f"{self.api}/icons/search?query={query}&count={count}&offset={offset}"
		if premium:
			url += f"&premium={premium}"
		if vector:
			url += f"&vector={vector}"
		if license:
			url += f"&license={license}"
		if category:
			url += f"&category={category}"
		if style:
			url += f"&style={style}"
		if is_explicit:
			url += f"&is_explicit={is_explicit}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_icon_details(self, icon_id: int) -> dict:
		return requests.get(
			f"{self.api}/icons/{icon_id}",
			headers=self.headers).json()
			
	def get_iconset_icons(
			self,
			iconset_id: int,
			query: str = None,
			count: int = 10,
			offset: int = 0,
			vector: str = None) -> dict:
		"""
		Get the list of all icons in an icon set sorted descendingly by the popularity of the icons
		Parameters:
			iconset_id: (int): integer <the icon set id (number) or the identifier (string)>
			query: (str): string <the search query>
			count: (int): integer <int32> -> <number of icons to include in the result>
			offset: (int): integer <int32> -> <result offset. starts from 0, resulting in the first count icons being returned>
			vector: (str): string <all, empty - include all icons> <0, false - only include raster icons> <1, true - only include vector icons>
		Returns: 
			dict: list of Icon objects in icons and a count of the icons returned in total_count
		"""
		url = f"{self.api}/iconsets/{iconset_id}/icons?count={count}&offset={offset}"
		if query:
			url += f"&query={query}"
		if vector:
			url += f"&vector={vector}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_public_iconsets(
			self,
			count: int = 10,
			after: int = None,
			premium: str= None,
			vector: str = None,
			license: str = None) -> dict:
		"""
		Get the list of all public icon sets in descending order of when they were published
		Parameters:
			count: (int): integer <int32> -> <number of icons to include in the result>
			after: (int): integer <int32> -> <Icon set ID of the last icon set received. If empty, the count most recently published icon sets are returned>
			premium: (str): string <all, empty - include all icons> <0, false - only include nonpremium icons> <1, true - only include premium icons>
			vector: (str): string <all, empty - include all icons> <0, false - only include raster icons> <1, true - only include vector icons>
			license: (str): string <none, empty - include all icons> <commercial - only include icons that can be used commercially> <commercial-nonattribution - only include icons that be used commercially without any attribution requirements>
		Returns: 
			dict: list of Iconset objects in iconsets and a count of the iconsets returned in total_count
		"""
		url = f"{self.api}/iconsets?count={count}"
		if after:
			url += f"&after={after}"
		if premium:
			url += f"&premium={premium}"
		if vector:
			url += f"&vector={vector}"
		if license:
			url += f"&license={license}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_iconset_details(self, iconset_id: int) -> dict:
		return requests.get(
			f"{self.api}/iconsets/{iconset_id}",
			headers=self.headers).json()
			
	def get_category_iconsets(
			self,
			category_identifier: str,
			count: int = 10,
			after: int = None,
			premium: str= None,
			vector: str = None,
			license: str = None) -> dict:
		"""
		Get the list of public icon sets in a category in descending order of when they were published
		Parameters:
			category_identifier: (str): string <category identifier>
			count: (int): integer <int32> -> <number of icons to include in the result>
			after: (int): integer <int32> -> <Icon set ID of the last icon set received. If empty, the count most recently published icon sets are returned>
			premium: (str): string <all, empty - include all icons> <0, false - only include nonpremium icons> <1, true - only include premium icons>
			vector: (str): string <all, empty - include all icons> <0, false - only include raster icons> <1, true - only include vector icons>
			license: (str): string <none, empty - include all icons> <commercial - only include icons that can be used commercially> <commercial-nonattribution - only include icons that be used commercially without any attribution requirements>
		Returns: 
			dict: list of Iconset objects in iconsets and a count of the iconsets returned in total_count
		"""
		url = f"{self.api}/categories/{category_identifier}/iconsets?count={count}"
		if after:
			url += f"&after={after}"
		if premium:
			url += f"&premium={premium}"
		if vector:
			url += f"&vector={vector}"
		if license:
			url += f"&license={license}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_user_iconsets(
			self,
			user_id: str,
			count: int = 10,
			after: int = None,
			premium: str= None,
			vector: str = None,
			license: str = None) -> dict:
		"""
		Get the list of all public icon sets owned by a specific user in descending order of when they were published
		Parameters:
			user_id: (str): string <id of the user>
			count: (int): integer <int32> -> <number of icons to include in the result>
			after: (int): integer <int32> -> <Icon set ID of the last icon set received. If empty, the count most recently published icon sets are returned>
			premium: (str): string <all, empty - include all icons> <0, false - only include nonpremium icons> <1, true - only include premium icons>
			vector: (str): string <all, empty - include all icons> <0, false - only include raster icons> <1, true - only include vector icons>
			license: (str): string <none, empty - include all icons> <commercial - only include icons that can be used commercially> <commercial-nonattribution - only include icons that be used commercially without any attribution requirements>
		Returns: 
			dict: list of Iconset objects in iconsets and a count of the iconsets returned in total_count
		"""	
		url = f"{self.api}/users/{user_id}/iconsets?count={count}"
		if after:
			url += f"&after={after}"
		if premium:
			url += f"&premium={premium}"
		if vector:
			url += f"&vector={vector}"
		if license:
			url += f"&license={license}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_author_iconsets(
			self,
			author_id: int,
			count: int = 10,
			after: int = None,
			premium: str= None,
			vector: str = None,
			license: str = None) -> dict:
		"""
		Get the list of all public icon sets owned by a specific author in descending order of when they were published
		Parameters:
			author_id: (int): integer <int32> -> <author id>
			count: (int): integer <int32> -> <number of icons to include in the result>
			after: (int): integer <int32> -> <Icon set ID of the last icon set received. If empty, the count most recently published icon sets are returned>
			premium: (str): string <all, empty - include all icons> <0, false - only include nonpremium icons> <1, true - only include premium icons>
			vector: (str): string <all, empty - include all icons> <0, false - only include raster icons> <1, true - only include vector icons>
			license: (str): string <none, empty - include all icons> <commercial - only include icons that can be used commercially> <commercial-nonattribution - only include icons that be used commercially without any attribution requirements>
		Returns: 
			dict: list of Iconset objects in iconsets and a count of the iconsets returned in total_count
		"""	
		url = f"{self.api}/authors/{author_id}/iconsets?count={count}"
		if after:
			url += f"&after={after}"
		if premium:
			url += f"&premium={premium}"
		if vector:
			url += f"&vector={vector}"
		if license:
			url += f"&license={license}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_author_iconsets(
			self,
			style_identifier: str,
			count: int = 10,
			after: int = None,
			premium: str= None,
			vector: str = None,
			license: str = None) -> dict:
		"""
		Get the list of public icon sets of a specific style in descending order of when they were published
		Parameters:
			style_identifier: (str): string <style identifier>
			count: (int): integer <int32> -> <number of icons to include in the result>
			after: (int): integer <int32> -> <Icon set ID of the last icon set received. If empty, the count most recently published icon sets are returned>
			premium: (str): string <all, empty - include all icons> <0, false - only include nonpremium icons> <1, true - only include premium icons>
			vector: (str): string <all, empty - include all icons> <0, false - only include raster icons> <1, true - only include vector icons>
			license: (str): string <none, empty - include all icons> <commercial - only include icons that can be used commercially> <commercial-nonattribution - only include icons that be used commercially without any attribution requirements>
		Returns: 
			dict: list of Iconset objects in iconsets and a count of the iconsets returned in total_count
		"""	
		url = f"{self.api}/styles/{style_identifier}/iconsets?count={count}"
		if after:
			url += f"&after={after}"
		if premium:
			url += f"&premium={premium}"
		if vector:
			url += f"&vector={vector}"
		if license:
			url += f"&license={license}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_author_details(self, author_id: int) -> dict:
		return requests.get(
			f"{self.api}/authors/{author_id}",
			headers=self.headers).json()
			
	def get_all_categories(
			self,
			count: int = 10,
			after: int = None) -> dict:
		url = f"{self.api}/categories?count={count}"
		if after:
			url += f"&after={after}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_category_details(
			self,
			category_identifier: str) -> dict:
		return requests.get(
			f"{self.api}/categories/{category_identifier}",
			headers=self.headers).json()
			
	def get_license_details(self, license_id: int) -> dict:
		return requests.get(
			f"{self.api}/licenses/{license_id}",
			headers=self.headers).json()
			
	def get_all_styles(
			self,
			count: int = 10,
			after: int = None) -> dict:
		url = f"{self.api}/styles?count={count}"
		if after:
			url += f"&after={after}"
		return requests.get(
			url, headers=self.headers).json()
			
	def get_style_details(
			self,
			style_identifier: str) -> dict:
		return requests.get(
			f"{self.api}/styles/{style_identifier}",
			headers=self.headers).json()
			
	def get_user_details(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/users/{user_id}",
			headers=self.headers).json()
