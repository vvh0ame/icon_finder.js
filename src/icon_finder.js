class IconFinder {
	constructor(apiKey) {
		this.api = "https://api.iconfinder.com/v4"
		this.headers = {
			"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
			"authorization": `Bearer ${this.apiKey}`
		}
	}

	async searchIcons(
			query,
			count = 1,
			offset = 0,
			premium = null,
			vector = null,
			license = null,
			category = null,
			style = null,
			isExplicit = null) {
		let url = `${this.api}/icons/search?query=${query}&count=${count}&offset=${offset}`
		if (premium) {
			url += `&premium=${premium}`
		}
		if (vector) {
			url += `&vector=${vector}`
		}
		if (license) {
			url += `&license=${license}`
		}
		if (category) {
			url += `&category=${category}`
		}
		if (style) {
			url += `&style=${style}`
		}
		if (isExplicit) {
			url += `&is_explicit=${isExplicit}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getIconDetails(iconId) {
		const response = await fetch(
			`${this.api}/icons/${iconId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getIconSetIcons(
			iconSetId,
			count = 10,
			query = null,
			offset = 0,
			vector = null) {
		let url = `${this.api}/iconsets/${iconSetId}?count=${count}&offset=${offset}`
		if (query) {
			url += `&query=${query}`
		}
		if (vector) {
			url += `&vector=${vector}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPublicIconSets(
			count = 10,
			after = null,
			premium = null,
			vector = null,
			license = null) {
		let url = `${this.api}/iconsets?count=${count}`
		if (after) {
			url += `&after=${after}`
		}
		if (premium) {
			url += `&premium=${premium}`
		}
		if (vector) {
			url += `&vector=${vector}`
		}
		if (license) {
			url += `&license=${license}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getIconSetDetails(iconSetId) {
		const response = await fetch(
			`${this.api}/iconsets/${iconSetId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCategoryIconSets(
			categoryIdentifier,
			count = 10,
			after = null,
			premium = null,
			vector = null,
			license = null) {
		let url = `${this.api}/categories/${categoryIdentifier}/iconsets?count=${count}`
		if (after) {
			url += `&after=${after}`
		}
		if (premium) {
			url += `&premium=${premium}`
		}
		if (vector) {
			url += `&vector=${vector}`
		}
		if (license) {
			url += `&license=${license}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserIconSets(
			userId,
			count = 10,
			after = null,
			premium = null,
			vector = null,
			license = null) {
		let url = `${this.api}/users/${userId}/iconsets?count=${count}`
		if (after) {
			url += `&after=${after}`
		}
		if (premium) {
			url += `&premium=${premium}`
		}
		if (vector) {
			url += `&vector=${vector}`
		}
		if (license) {
			url += `&license=${license}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAuthorIconSets(
			authorId,
			count = 10,
			after = null,
			premium = null,
			vector = null,
			license = null) {
		let url = `${this.api}/authors/${authorId}/iconsets?count=${count}`
		if (after) {
			url += `&after=${after}`
		}
		if (premium) {
			url += `&premium=${premium}`
		}
		if (vector) {
			url += `&vector=${vector}`
		}
		if (license) {
			url += `&license=${license}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAuthorDetails(authorId) {
		const response = await fetch(
			`${this.api}/authors/${authorId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAllCategories(count = 10, after = null) {
		let url = `${this.api}/categories?count=${count}`
		if (after) {
			url += `&after=${after}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCategoryDetails(categoryIdentifier) {
		const response = await fetch(
			`${this.api}/categories/${categoryIdentifier}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getLicenseDetails(licenseId) {
		const response = await fetch(
			`${this.api}/licenses/${licenseId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAllStyles(count = 10, after = null) {
		let url = `${this.api}/styles?count=${count}`
		if (after) {
			url += `&after=${after}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getStyleDetails(styleIdentifier) {
		const response = await fetch(
			`${this.api}/styles/${styleIdentifier}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
 }

module.exports = {IconFinder}
