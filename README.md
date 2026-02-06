# CurrentLastFM Project
This is for fetching your current (or last played) last fm account! It's easy to use, and you don't need to be a genious on how to use it.

## How do I use it?
Simple! The url for fetching your current/last-played from your account is simple. <br>
`https://pylastfmcurrent.vercel.app/api/now_playing?user=YOUR_USERNAME&api_key=YOUR_API_KEY` <br>

Now, to parse this into your website, follow this tutorial.

First of all, we need an API key. Head on over to https://www.last.fm/api/account/create and make a create key.

Follow the red arrows and texts!

<img src="docs/creating a api.png">
<img src="docs/copying the api key.png">

> [!IMPORTANT]
> It's recommended to ALWAYS hide your API key. If you're making your website open source (like what I do), please make a `.env` file and `.gitignore` it.

Now, you need a JS/TS code for it. Here's both of them.

> [!IMPORTANT]
> This code is actually untested and was made by Google Gemini 3.0 Pro. Please let me know through [issues tab](https://github.com/daveberrys/CurrentLastFM/issues) if it works or not.

### JavaScript Example (Fetch API)
This example uses the modern `fetch` API in an `async` function to get the data.

```javascript
async function getNowPlaying(username, apiKey) {
    const apiUrl = `https://pylastfmcurrent.vercel.app/api/now_playing?user=${username}&api_key=${apiKey}`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`API request failed: ${response.statusText}`);
        }
        
        const data = await response.json();
        console.log(data);

        if (data.isPlaying) {
            console.log(`Currently playing: ${data.song} by ${data.artist}`);
        } else {
            console.log(`Last played: ${data.song} by ${data.artist}`);
        }
        
        return data;
    } catch (error) {
        console.error("Failed to fetch Last.fm data:", error);
        return null;
    }
}

// -- Usage --
// Replace with the user's details
const lastFmUsername = "YOUR_USERNAME";
const lastFmApiKey = "YOUR_API_KEY";

getNowPlaying(lastFmUsername, lastFmApiKey);
```

### TypeScript Example (Fetch API with Types)
For a more robust implementation in a TypeScript project, you should define a type for the data you expect to receive.

```typescript
// Define an interface for the API response shape
interface LastFmTrack {
    song: string;
    artist: string;
    albumArt: string;
    isPlaying: boolean;
    error?: string;
}

async function getNowPlayingTyped(username: string, apiKey: string): Promise<LastFmTrack | null> {
    const apiUrl = `https://pylastfmcurrent.vercel.app/api/now_playing?user=${username}&api_key=${apiKey}`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`API request failed: ${response.statusText}`);
        }
        
        const data: LastFmTrack = await response.json();

        if (data.error) {
            throw new Error(`Last.fm API returned an error: ${data.error}`);
        }

        console.log(data);

        if (data.isPlaying) {
            console.log(`Currently playing: ${data.song} by ${data.artist}`);
        } else {
            console.log(`Last played: ${data.song} by ${data.artist}`);
        }

        return data;
    } catch (error) {
        console.error("Failed to fetch Last.fm data:", error);
        return null;
    }
}

// -- Usage --
// Replace with the user's details
const lastFmUsernameTS: string = "YOUR_USERNAME";
const lastFmApiKeyTS: string = "YOUR_API_KEY";

getNowPlayingTyped(lastFmUsernameTS, lastFmApiKeyTS);
```