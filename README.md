# Personal Academic Website - Aman Gupta

A modern, responsive, and SEO-optimized personal academic website built with Bootstrap 5.

## Features

### ✨ Responsive Design
- Mobile-first approach with Bootstrap 5
- Fully responsive across all devices (mobile, tablet, desktop)
- Touch-friendly navigation and interactive elements
- Optimized layout for readability on all screen sizes

### 🔍 SEO Optimization
- Comprehensive meta tags and Open Graph protocol support
- Schema.org structured data for better search engine understanding
- XML sitemap for easy crawling
- robots.txt for search engine guidance
- Semantic HTML5 markup
- Fast loading with modern CDNs and minimal dependencies

### 🎨 Modern Design
- Clean, professional layout
- Smooth animations and transitions
- Consistent color scheme with CSS variables
- Beautiful typography with Google Fonts
- Font Awesome icons

### ♿ Accessibility
- Semantic HTML elements
- ARIA labels and roles
- High contrast text
- Keyboard navigation support
- Image alt text

### 🔒 Security & Privacy
- Email address protection (obfuscated on display)
- External links with `rel="noopener noreferrer"`
- Content Security Policy ready

## File Structure

```
├── index.html              # Main homepage
├── cv.html                 # CV/Resume page
├── sitemap.xml             # XML sitemap for search engines
├── robots.txt              # Robots configuration
├── AmanResume.pdf          # PDF resume (add your file)
├── 20230127_173822.jpg     # Profile image
└── README.md               # This file
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
