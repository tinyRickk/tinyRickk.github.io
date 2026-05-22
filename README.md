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
Edit `index.html` and update:
- Hero section text
- Research interests cards
- Skills tags
- Education & experience
- Social links
- Contact email

### Change Theme Colors
Edit CSS variables in `index.html` `<style>` section:
```css
:root {
  --primary-gradient: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
  --primary-color: #00d4ff;
  --secondary-color: #ff006e;
  --text-light: #e0e0e0;
  /* More variables available */
}
```

### Update Google Scholar Integration
Edit `scripts/fetch_publications.py`:
```python
SCHOLAR_ID = "_6mZBnoAAAAJ"  # Replace with your Scholar ID
```

### Add Custom Sections
Copy an existing section block and modify:
```html
<section id="your-section">
  <div class="container">
    <h2 class="section-title">Your Section Title</h2>
    <!-- Add your content -->
  </div>
</section>
```

## 🔄 Google Scholar Integration Setup

### Enable GitHub Actions (Already Done!)

The workflow file is pre-configured at `.github/workflows/update-publications.yml`

**Workflow Details:**
```yaml
# Runs on: 1st of every month at 00:00 UTC
# Trigger: Automatic + Manual option
# Action: Fetches papers, updates JSON, auto-commits
```

### Verify It's Working
1. Push code to GitHub
2. Go to repository → "Actions" tab
3. Select "Update Publications from Google Scholar"
4. You should see workflow runs on the 1st of each month

### Troubleshooting GitHub Actions

| Issue | Solution |
|-------|----------|
| Workflow not running | Check Settings → Actions → Runner settings enabled |
| Authorization denied | The default GitHub token has all needed permissions |
| Papers not fetching | Verify Scholar ID is correct in Python script |
| JSON file not updating | Check workflow logs in Actions tab for errors |

### Manual Publication Updates

You can always manually edit `data/publications.json`:
```json
{
  "last_updated": "2024-05-22T00:00:00Z",
  "total_papers": 3,
  "papers": [
    {
      "title": "Paper Title",
      "authors": "You, et al.",
      "year": "2024",
      "venue": "Journal Name",
      "citation_count": 5,
      "url": "https://doi.org/...",
      "type": "journal"
    }
  ]
}
```

## 📊 SEO & Google Search Console

### Setup Steps
1. **Add Property**: [search.google.com/search-console](https://search.google.com/search-console)
   - Add property: `https://tinyrickk.github.io`
2. **Verify**: Already done via meta tag in HTML
3. **Submit Sitemap**: Go to Sitemaps section → Submit `sitemap.xml`
4. **Monitor Coverage**: Check  which pages are indexed

### Test Indexing
Verify your site appears in Google search:
```
site:tinyrickk.github.io
site:tinyrickk.github.io "Aman Gupta"
"quantum communications" "Aman Gupta" UNSW
```

### Optimize Keywords
- Research interests mentioned throughout
- Education and institution highlighted
- Links to Google Scholar, GitHub, LinkedIn included
- Schema.org markup provides machine-readable data

## 🎨 Design Features

### Dark Mode Color Palette
- **Primary**: Cyan (#00d4ff) with gradient
- **Secondary**: Hot pink (#ff006e)
- **Background**: Deep blue (#0a0e27)
- **Text**: Light gray (#e0e0e0)

### Animations
- Slide-in effects on hero section
- Hover transformations on cards
- Intersection observer for scroll animations
- GPU-accelerated transitions

### Responsive Breakpoints
- **Mobile**: < 576px
- **Tablets**: 576px - 991px
- **Desktop**: > 991px
- **Large**: > 1400px

## 📈 Performance Metrics

### Current Optimizations
- CSS Containment: Scoped rendering limits
- Resource Hints: Preconnect, DNS prefetch
- Image Optimization: Aspect ratio locks, lazy loading
- Font Loading: `display=swap` prevents FOUT
- Minimal JavaScript: < 2KB of custom code

### Expected Core Web Vitals
- **LCP** (Largest Contentful Paint): < 2.5s ✅
- **FID** (First Input Delay): < 100ms ✅
- **CLS** (Cumulative Layout Shift): < 0.1 ✅

## 🔒 Privacy & Security

✅ **No tracking code** (no Google Analytics or similar)
✅ **No cookies** (except session/functional)
✅ **HTTPS enforced** (GitHub Pages feature)
✅ **Email not exposed** (displayed as secure text)
✅ **External links safe**: `rel="noopener noreferrer"`

## 📱 Mobile Experience

- Touch-friendly navigation
- Responsive images and layouts
- Fast loading on mobile networks
- PWA-ready with `manifest.json`
- Works offline (with service worker enhancement)

## 🌐 Browser Support

| Browser | Support |
|---------|---------|
| Chrome/Edge | 90+ |
| Firefox | 88+ |
| Safari | 14+ |
| Mobile Browsers | iOS 12+, Android 8+ |

## 📝 Maintenance Checklist

- [ ] Update publications monthly (or auto via GitHub Actions)
- [ ] Review Google Search Console quarterly
- [ ] Check analytics for top pages
- [ ] Update skills and experience annually
- [ ] Refresh bio section with new research focus
- [ ] Monitor for broken links (Tools → Link Checker)

## 🤝 Contributing

Want to improve this template?
1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Submit a pull request

## 📚 Resources

- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Google Fonts](https://fonts.google.com/)
- [Schema.org Markup](https://schema.org/)
- [GitHub Pages Docs](https://pages.github.com/)
- [GitHub Actions Docs](https://docs.github.com/actions)

## 📧 Contact & Support

**For this portfolio:**
- GitHub: [tinyRickk](https://github.com/tinyRickk)
- Email: aman.gupta@unsw.edu.au

## 📄 License

This project is open source and available under the MIT License.

---

**Version**: 2.0 (Dark Mode + Google Scholar Auto-Sync)
**Last Updated**: May 2024
**Status**: ✅ Production Ready

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
