---
type: Summary
title: "Responsive images — srcset and sizes (MDN)"
description: "In this article, we'll learn about the concept of responsive images — images that work well on devices with widely differing screen sizes, resolutions, and other such features — and look at"
resource: "https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images"
source_file: "Raw/06_product_patterns/mdn-responsive-images.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Responsive images — srcset and sizes (MDN)

Extractive digest of the immutable capture in
`Raw/06_product_patterns/mdn-responsive-images.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images>

## Opening

> In this article, we'll learn about the concept of responsive images — images that work well on devices with widely differing screen sizes, resolutions, and other such features — and look at what tools HTML provides to help implement them. This helps to improve performance across different devices.
> Let's examine a typical scenario. A typical website may contain a header image and some content images below the header. The header image will likely span the whole of the width of the header, and the content image will fit somewhere inside the content column. Here's an example:
> This works well on a wide screen device, such as a laptop or desktop (you can [see the example live](https://mdn.github.io/learning-area/html/multimedia-and-embedding/responsive-images/not-responsive.html "External link \(opens in new tab\)") and find the [source ...
> However, issues arise when you start to view the site on a narrow screen device. The header below looks OK, but it's starting to take up a lot of the screen height for a mobile device. And at this size, it is difficult to see faces of the two people within the first content image.

## Contents of the source document

- Using responsive images in HTML
  - Why responsive images?
  - How do you create responsive images?
    - Resolution switching: Different sizes
    - Resolution switching: Same size, different resolutions
    - Art direction
    - Why can't we just do this using CSS or JavaScript?
  - Implementing your own responsive images
  - Summary
  - See also
  - Help improve MDN

## Related pages

[[Responsive Design]]
