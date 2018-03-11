<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>My Table</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
        <th>Image</th>
        <th>Name</th>
        <th>Price</th>
    </tr>
    <xsl:for-each select="data/elem">
    <tr>
        <td><xsl:value-of select="image"/></td>
        <td><xsl:value-of select="text"/></td>
        <td><xsl:value-of select="price"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>