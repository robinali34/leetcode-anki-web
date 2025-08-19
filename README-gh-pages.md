# 🌐 GitHub Pages Branch - Static Website

This branch contains the static version of the LeetCode Anki Card Generator for hosting on GitHub Pages.

## 🚀 Quick Deploy

1. **Push this branch to GitHub:**
   ```bash
   git push origin gh-pages
   ```

2. **Enable GitHub Pages:**
   - Go to your repository Settings
   - Navigate to Pages section
   - Select "Deploy from a branch"
   - Choose `gh-pages` branch
   - Save

3. **Your site will be available at:**
   ```
   https://yourusername.github.io/lc-anki/
   ```

## 📁 Static Files

- **`index.html`** - Main landing page with rainbow tag system
- **`LICENSE`** - MIT License file
- **`.github/workflows/deploy.yml`** - Auto-deployment workflow

## 🎨 Features

### ✅ What Works (Static)
- **Rainbow Tag System** - 7-color scheme based on problem counts
- **Sample Problems** - 6 demo problems with full styling
- **Responsive Design** - Mobile-friendly Bootstrap layout
- **Interactive Elements** - Hover effects and animations
- **Tag Filtering** - Visual tag organization

### ⚠️ What's Limited (Static vs Flask)
- **Problem Details** - Shows demo alert instead of full page
- **Anki Card Generation** - Not available in static version
- **Dynamic Data** - Uses sample data instead of live database
- **User Progress** - No backend storage

## 🔧 Customization

### Update Sample Problems
Edit the `sampleProblems` array in `index.html`:

```javascript
const sampleProblems = [
    {
        id: 1,
        title: "Your Problem Title",
        difficulty: "Easy",
        description: "Your problem description...",
        tags: ["Array", "Hash Table"],
        acceptance: "52.3%"
    }
    // Add more problems...
];
```

### Update Tag Data
Modify the `tagData` object for different tag counts and colors:

```javascript
const tagData = {
    "Your Tag": 150,  // Will be red (>150)
    "Another Tag": 45, // Will use rainbow colors (≤150)
    // Add more tags...
};
```

### Change Colors
Update the CSS variables in the `<style>` section:

```css
.btn-outline-danger { color: #your-color; border-color: #your-color; }
.btn-outline-warning { color: #your-color; border-color: #your-color; }
/* etc... */
```

## 🚀 Deployment Options

### Option 1: GitHub Actions (Recommended)
The `.github/workflows/deploy.yml` file automatically deploys when you push to `gh-pages`.

### Option 2: Manual Deploy
1. Push to `gh-pages` branch
2. Manually enable GitHub Pages in repository settings
3. Select `gh-pages` as source

### Option 3: Custom Domain
1. Add `CNAME` file with your domain
2. Configure DNS settings
3. Update repository settings

## 📱 Mobile Optimization

The static site is fully responsive with:
- **Bootstrap 5** responsive grid system
- **Mobile-first** design approach
- **Touch-friendly** buttons and interactions
- **Optimized** for all screen sizes

## 🔍 SEO Features

- **Meta tags** for social sharing
- **Semantic HTML** structure
- **Alt text** for accessibility
- **Open Graph** meta tags
- **Twitter Card** support

## 🎯 Performance

- **CDN Resources** - Bootstrap and Font Awesome from CDN
- **Minimal JavaScript** - Lightweight interactive features
- **Optimized CSS** - Efficient styling with CSS3 features
- **Fast Loading** - No backend dependencies

## 🔗 Links

- **Live Demo**: https://yourusername.github.io/lc-anki/
- **Full App**: https://github.com/yourusername/lc-anki
- **Main Branch**: Contains the full Flask application

## 📝 Notes

- This is a **demo/landing page** version
- For full functionality, use the main branch with Flask
- Perfect for showcasing the project and rainbow tag system
- Easy to customize and deploy

---

**Ready to deploy? Just push this branch and enable GitHub Pages! 🚀** 