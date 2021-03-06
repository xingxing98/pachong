from lxml import etree

text = ''' 
<div> 
  <ul> 
    <li class="item-1">
      <a href="link1.html">first item</a>
    </li> 
    <li class="item-1">
      <a href="link2.html">second item</a>
    </li> 
    <li class="item-inactive">
      <a href="link3.html">third item</a>
    </li> 
    <li class="item-1">
      <a href="link4.html">fourth item</a>
    </li> 
    <li class="item-0">
      <a href="link5.html">fifth item</a>
    </li>
  </ul> 
</div>
'''

html = etree.HTML(text)

# etree.HTML()能够自动补全html确实的标签
print(etree.tostring(html))
