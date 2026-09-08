function Link(el)
  el.target = el.target:gsub("%.md([#?]?)", ".html%1")
  return el
end
