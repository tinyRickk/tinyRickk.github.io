# Aman Gupta - Professional Quantum Communications Portfolio

A modern, professional dark-mode portfolio website showcasing research in quantum communications, cryptography, and experimental quantum optics. **Features automatic paper synchronization from Google Scholar via GitHub Actions.**

## ✨ Features

### 🎨 Modern Professional Design
- **Dark Mode Theme**: Sleek, modern design with elegant color gradients
- **Smooth Animations**: GPU-accelerated transitions and hover effects
- **Fully Responsive**: Perfect on desktop, tablet, and mobile
- **High Performance**: Optimized for Core Web Vitals

### 📄 Content Sections
- **Hero Section**: Eye-catching introduction with action buttons
- **Research Interests**: 6 key research areas with descriptive cards
- **Technical Skills**: 12+ skill tags highlighting expertise
- **Education & Experience**: Timeline-style professional history
- **Publications**: Auto-synced from Google Scholar (monthly)
- **Contact**: Professional contact section with social links

### 🤖 Automation Features
- **Google Scholar Sync**: Monthly automatic paper fetching
- **GitHub Actions**: Runs on schedule or manual trigger
- **Zero Manual Work**: Papers update without code changes
- **Smart Caching**: Efficient data storage with JSON

### 🔍 SEO & Discovery
- **Google Search Console Ready**: Meta tags, sitemap, verification
- **Schema.org Markup**: Rich snippets for better indexing
- **Open Graph & Twitter Cards**: Better social media sharing
- **Fast Loading**: CDN delivery, resource hints, optimization

### ♿ Accessibility
- **Semantic HTML5**: Proper heading hierarchy
- **ARIA Compliant**: Screen reader support
- **Keyboard Navigation**: Full keyboard support
- **High Contrast**: Dark theme with readable text

## 🚀 Quick Start

### Deploy in 2 Minutes
```bash
git clone https://github.com/tinyRickk/tinyRickk.github.io.git
cd tinyRickk.github.io
# Make changes if needed
git push  # Deploys to GitHub Pages
```

### Automatic Google Scholar Sync (Already Configured!)

**How It Works:**
- 📅 Runs **automatically every month** (1st day at 00:00 UTC)
- 🔄 Fetches your latest papers from Google Scholar
- 💾 Updates `data/publications.json` automatically
- 📱 Website displays new papers without manual intervention

**Your Scholar ID:** `_6mZBnoAAAAJ` (From your profile URL)

**To Manually Trigger Updates:**
1. Go to your GitHub repository
2. Click "Actions" tab
3. Select "Update Publications from Google Scholar"
4. Click "Run workflow" button
5. Papers update in < 5 minutes

## 📁 Project Structure

```
├── index.html                    # Main portfolio page
├── cv.html                       # CV/Resume page
├── manifest.json                 # Progressive Web App config
├── sitemap.xml                   # XML sitemap for SEO
├── robots.txt                    # Search engine crawling rules
├── README.md                     # This file
├── scripts/
│   └── fetch_publications.py     # Google Scholar scraper
├── .github/workflows/
│   └── update-publications.yml   # GitHub Actions automation
└── data/
    └── publications.json         # Publications (auto-updated)
```

## Getting Started

### Local Development
1. Clone the repository
2. Open `index.html` in your browser
3. No build tools or dependencies required!

### Deployment
Simply push to GitHub Pages:
```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

Your site will be live at `https://yourusername.github.io/`

## Customization

### Update Personal Information
Edit `index.html` and `cv.html`:
- Name and title
- Contact information
- Bio and research interests
- Social media links
- Publication details

### Add/Update Profile Image
Replace `20230127_173822.jpg` with your own image:
- Recommended size: 400x400px or larger
- Format: JPG, PNG, or WebP

### Add Resume PDF
Replace `AmanResume.pdf` with your resume:
- Name must match the reference in `cv.html`

### Modify Colors
Edit CSS variables in `<style>` section:
```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --text-dark: #212529;
  --bg-light: #f8f9fa;
}
```

### Update Publications
Edit the publications section in `index.html` to add/remove entries

## SEO Best Practices Implemented

✅ Meta descriptions (improves CTR from search results)
✅ Open Graph tags (better social media sharing)
✅ Schema.org structured data (rich snippets in search)
✅ Mobile optimization (critical ranking factor)
✅ Fast loading times (CDN-based resources)
✅ Semantic HTML5 (helps search engines understand content)
✅ Internal linking (improves site structure)
✅ Proper heading hierarchy (H1 → H2 → H3)
✅ Image optimization (alt text and proper sizing)
✅ Canonical URLs (prevents duplicate content issues)

## Performance Optimization

- Uses Bootstrap 5 from CDN (minimal file size)
- Modern CSS Grid and Flexbox
- Lazy-loaded external resources
- Optimized for fast initial load
- Minimal inline scripts

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Maintenance

### Update Information
Keep your content fresh:
- Update publication list quarterly
- Refresh research interests annually
- Keep CV current

### Monitor Rankings
- Google Search Console: submit sitemap, monitor impressions
- Google Analytics: track visitor behavior
- Bing Webmaster Tools: additional search visibility

## Technical Stack

- **Framework**: Bootstrap 5.3
- **Icons**: Font Awesome 6.4
- **Fonts**: Google Fonts (Open Sans, Oswald)
- **No JavaScript frameworks**: Pure vanilla JS
- **No build tools needed**: Just HTML, CSS, JS

## Accessibility Checklist

- ✅ Proper heading hierarchy
- ✅ Alt text for images
- ✅ Semantic HTML elements
- ✅ Color contrast meets WCAG AA
- ✅ Keyboard navigable
- ✅ Responsive design
- ✅ Focus indicators on interactive elements

## Future Enhancements

- [ ] Blog section for research updates
- [ ] Project portfolio with detailed descriptions
- [ ] Email contact form (requires backend)
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Research collaboration showcase

## Attribution

Originally based on **Plain Academic** theme, significantly updated with:
- Bootstrap 5 (from Bootstrap 3)
- Modern CSS and responsive design
- Comprehensive SEO optimization
- Better accessibility
- Improved performance

## License

Use this template freely for your own academic website!

## Support

For questions or improvements, feel free to contribute or reach out!

---

**Last Updated**: May 22, 2024
**Version**: 2.0 (Modern SEO & Responsive)
