def get_vulnerable_functions(language):
    if language == "Python":
        return python_vulnerable_functions
    elif language == "Node.js":
        return nodejs_vulnerable_functions
    elif language == "Java":
        return java_vulnerable_functions
    elif language == "C#":
        return csharp_vulnerable_functions
    elif language == "PHP":
        return php_vulnerable_functions
    else:
        return {}


# Python vulnerable functions
python_vulnerable_functions = {
    "Open Redirect": [
        "redirect(",  
    ],
    "SQL Injection": [    
        "executescript(", 
        "cmd_query(", "cmd_query_iter(", "get_rows(", "cmd_process_result(",
        "callproc(", "mogrify(",
        "text(", "select(", "update(", "insert(", "delete(",
        "RawSQL(",
        "execute_sql(", 
        "select(", "sqlmeta(", "selectBy(", "selectOne(",
        "execute_insert(", "execute_direct(",
        "execute_values(", "execute_batch(",
        "query(","scalar(",
        "execute(", "executemany(",
       
],

    "Path Traversal": [
         "open(", 
        "remove(", 
        "rmdir(", 
        "mkdir(", 
        "makedirs(", 
        "lstat(", 
        "chmod(", 
        "chown(", 
        "rename(", 
        "replace(", 
        "symlink(", 
        "unlink(", 
        "utime(", 
        "join(", 
        "realpath(", 
        "abspath(", 
        "copy2(", 
        "move(", 
        "rmtree(",
    ],
    "Server-Side Request Forgery (SSRF)": [
         "request(", 
        "get(", 
        "head(", 
        "post(", 
        "put(", 
        "patch(", 
        "delete(", 
        "options(", 
        "session(", 
        "Session("
    ],
    "Command Injection": [
        "system(", 
        "popen(", 
        "popen2(", 
        "popen3(", 
        "popen4(", 
        "execl(", 
        "execle(", 
        "execlp(", 
        "execlpe(", 
        "execv(", 
        "execve(", 
        "execvp(", 
        "execvpe(", 
        "spawnl(", 
        "spawnle(", 
        "spawnlp(", 
        "spawnlpe(", 
        "spawnv(", 
        "spawnve(", 
        "spawnvp(", 
        "spawnvpe("
    ],
    "Insecure Deserialization": [
        "loads(",  
        "load(", 
        "decode(",  
        "unserializeData(", 
        "open(",  
        "dump("
    ],
    "XML External Entity (XXE)": [
       "parse(", 
        "fromstring(", 
        "parseString(", 
        "XML(", 
        "XMLParser("
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Python XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        "render_template(", 
        "render_template_string(", 
        "Template(", 
        "Environment.from_string(", 
        "Environment.get_template(", 
        "TemplateResponse("
        "render_template(", 
        "get_template(",  # Mako
        "get_templates(",  # Mako
        "load(",  # Tornado
        "template(",  # Bottle
        "view(",  # Bottle
        "render(",  # Pyramid
        "render_to_response(",  # Pyramid
        "PageTemplate(",  # Chameleon
        "PageTemplateFile("  # Chameleon
    ],
    "Privilege Escalation": [
        # Add Python privilege escalation vulnerable functions here
    ]
}

# JavaScript (Node.js) vulnerable functions
nodejs_vulnerable_functions = {
    "Open Redirect": [
        "redirect(",
        "location(",
        ],
     "SQL Injection": [
        "query(", 
        "execute(", 
        "raw(", 
        "one(", 
        "many(", 
        "fetchAll(", 
        "where(",
        "native(", 
        "createQueryBuilder(", 
        "$queryRaw(", 
        "$queryRawRaw(", 
        "exec(" 
    ],
    "Path Traversal": [
        "sendFile(",
        "send(",
        "sendFile(",
        "file(",
        "serve-static(",
        "express-static(",
        "express.static(",
        "koa-static(",
        "readFile(",
        "readFileSync(",
        "writeFile(",
        "writeFileSync(",
        "unlink("
    ],
    "Server-Side Request Forgery (SSRF)": [
        "request(",
        "get(",
        "post(",
    ],
    "Command Injection": [
    "exec(",
        "execSync(",
        "spawn(",
        "execFile(",
        "exec(",
  ],
    "Insecure Deserialization": [
        "parse(",
        "unserialize(",
        "parse(",
        "deserialize(",
        "session(",
        "parse(",
        "populate(",
        "Model.build(",
        "Model.create(",
        "deserializeUser(",
    ],
    "XML External Entity (XXE)": [
        "parseXML(",
        "parseString(",
        "parse(",
        "parseXmlString(",
        "parser(",
    ],
    "Cross-Site Scripting (XSS)": [
        # Add JavaScript (Node.js) XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        "render(",
        "view(",
    ],
    "Privilege Escalation": [
        # Add JavaScript (Node.js) privilege escalation vulnerable functions here
    ]
}


java_vulnerable_functions  = {
    
    "SQL Injection": [
        "execute(", "executeQuery(", "executeUpdate(", "addBatch(", "nativeSQL(", 
        "createNativeQuery(", "createQuery(", "update(", "query(", "selectList(", 
        "selectMap(", "selectOne(", "delete(", "insert(", "createSQLQuery("
    ],
    "XML External Entity (XXE)": [
        "newDocumentBuilder(", "newSAXParser(", "newXMLReader(", "newTransformer(", 
        "newSchema(", "newXPath(", "createXMLStreamReader(", "createXMLEventReader(", 
        "createXMLEventWriter(", "createXMLStreamWriter("
    ],
    "Insecure Deserialization": [
        "readObject(", "readUnshared(", "XMLDecoder(", "fromXML(", "readValue(", 
        "readObjectOrNull(", "copy(", "load(", "readObject(", "readArray(", "fromJson(", 
        "parseObject(", "unmarshal(", "parse(", "MappedXMLStreamReader(", "fromXML(", 
        "unmarshal(", "InvokerTransformer(", "DefaultMessageListenerContainer(", 
        "Interceptor(", "readElement("
    ],
    "Command Injection": [
        "exec(", "start(", "parse(", "execute(", "launch(", "executeCommand(", 
        "evaluate(", "me("
    ],
    "Server-Side Request Forgery (SSRF)": [
        "openConnection(", "send(", "getForObject(", "postForObject(", "exchange(", "execute("
    ],
    "Open Redirect": [
        "sendRedirect(", "setRedirectStrategy(", "setDefaultTargetURL("
    ],
    "Path Traversal": [
        "getRealPath(", "getFile(", "getInputStream(", "load(", "copyToFile(", 
        "writeStringToFile(", "readFileToString("
    ],
    "Server-Side Template Injection (SSTI)": [
        "render(", "merge(",   
        "process(",                         
        "processTemplate(",                  
        "include(", "forward(",              
        "evaluate(",             
        "include(",                          
    ],
  "Cross-Site Scripting (XSS)": [
   ],
    "Privilege Escalation": [
    ]

    
}


# C# vulnerable functions
csharp_vulnerable_functions = {
    "Open Redirect": [
        # Following are vulnerable to open redirects if user input is used unsanitized.
        "Redirect(",  # System.Web.Mvc.Controller.Redirect
        "Action(",  # System.Web.Mvc.Controller.Action
        "RouteUrl("  # System.Web.Mvc.UrlHelper.RouteUrl
    ],
    "SQL Injection": [
        "CommandText(",  # System.Data.IDbCommand.CommandText - Vulnerable to SQL injection if user input is used unsanitized.
        "ExecuteScalar(",  # System.Data.IDbCommand.ExecuteScalar - Vulnerable to SQL injection if user input is used unsanitized.
        "ExecuteReader(",  # System.Data.IDbCommand.ExecuteReader - Vulnerable to SQL injection if user input is used unsanitized.
        "ExecuteNonQuery("  # System.Data.IDbCommand.ExecuteNonQuery - Vulnerable to SQL injection if user input is used unsanitized.
        "SqlCommand(",
        "ExecuteSqlRaw(",
        "ExecuteSqlInterpolated(",
        "Query(",
        "FromSql("
    ],
    "Path Traversal": [
        # Following are vulnerable to path traversal if user input is used unsanitized.
        "CreateDirectory(",  # System.IO.Directory.CreateDirectory
        "CreateSubdirectory(",  # System.IO.DirectoryInfo.CreateSubdirectory
        "Copy(",  # System.IO.File.Copy
        "Create(",  # System.IO.File.Create
        "Delete(",  # System.IO.File.Delete
        "Move(",  # System.IO.File.Move
        "Open(",  # System.IO.File.Open
        "Combine(",  # System.IO.Path.Combine
        "ctor("  # ICSharpCode.SharpZipLib.Zip.FastZip::.ctor
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Following are vulnerable to SSRF if user input is used unsanitized.
        "Create(",  # System.Net.WebRequest.Create
        "GetResponse(",  # System.Net.WebRequest.GetResponse
        "DownloadData(",  # System.Net.WebClient.DownloadData
        "UploadData(",  # System.Net.WebClient.UploadData
        "GetAsync(",  # System.Net.Http.HttpClient.GetAsync
        "PostAsync(",  # System.Net.Http.HttpClient.PostAsync
        "RestClient(",  # RestClient
        "DownloadFile(",  # System.Net.WebClient.DownloadFile
        "DownloadString("  # System.Net.WebClient.DownloadString
    ],
    "Command Injection": [
        # Following are vulnerable to command injection if user input is used unsanitized.
        "Start(",  # System.Diagnostics.Process.Start
        "CreateProcess(",  # Microsoft.Win32.NativeMethods.CreateProcess
        "CreateProcessAsUser("  # Microsoft.Win32.NativeMethods.CreateProcessAsUser
        "FileName(",  # System.Diagnostics.ProcessStartInfo.FileName
        "Arguments(",  # System.Diagnostics.ProcessStartInfo.Arguments
        "SetPriviliege(",  # System.Security.AccessControl.Privilege.SetPriviliege
        "AdjustTokenPrivilege("  # Microsoft.Win32.NativeMethods.AdjustTokenPrivilege
  
    ],
    "Insecure Deserialization": [
        # Following are vulnerable to insecure deserialization if user input is used unsanitized.
        "Deserialize(",  # System.Runtime.Serialization.Json.DataContractJsonSerializer.Deserialize
        "ReadObject(",  # System.Runtime.Serialization.Json.DataContractJsonSerializer.ReadObject
        "DeserializeObject(",  # Newtonsoft.Json.JsonConvert.DeserializeObject
        "ToObject(",  # fastJSON.JSON.Instance.ToObject
        "UnPickle(",  # binarySerializer.UnPickle
        "FsPickler(",  # FsPickler
        "CreateJsonSerializer(",  # CreateJsonSerializer
        "NetDataContractSerializer(",  # NetDataContractSerializer
        "DataContractSerializer(",  # DataContractSerializer
        "SoapFormatter(",  # SoapFormatter
        "Jayson(",  # Jayson
        "DataContractResolver(",  # DataContractResolver
        "BinaryServerFormatterSinkProvider("  # BinaryServerFormatterSinkProvider
    ],
    "XML External Entity (XXE)": [
        "XmlResolver(",  # System.Xml.XmlReaderSettings.XmlResolver - Vulnerable to XXE if user input is used unsanitized.
        "Load(",  # System.Xml.Linq.XDocument.Load - Vulnerable to XXE if user input is used unsanitized.
        "LoadXml("  # System.Xml.XmlDocument.LoadXml - Vulnerable to XXE if user input is used unsanitized.
    ],
     "Cross-Site Scripting (XSS)": [
        "Write(",  # System.Web.UI.HtmlTextWriter.Write - Vulnerable to XSS if user input is used unsanitized.
        "ToString("  # System.Object.ToString - Vulnerable to XSS if user input is used unsanitized.
    ],
    "Server-Side Template Injection (SSTI)": [
        "RenderBody(",  # ASP.NET Razor - RenderBody method
        "RenderPage(",  # ASP.NET Razor - RenderPage method
        "RenderSection(",  # ASP.NET Razor - RenderSection method
        "Parse(",  # DotLiquid - Template.Parse method
        "Render(",  # DotLiquid - Template.Render method
        "TransformText(",  # T4 Text Templates - TransformText method
        "RenderTemplate(",  # Scriban - TemplateContext.RenderTemplate method
        "Render(" ,  # Scriban - Template.Render method
        "RenderFromSource(",  # Nustache - Render.StringFromSource method
        "FormatWith(",  # StringTemplate - ST.FormatWith method
        "Render(" ,  # Stubble - StubbleBuilder.Render method
        "ToString(",  # Antlr StringTemplate - Template.ToString method
        "RenderAsync(",  # Fluid - FluidTemplate.RenderAsync method
    ],
    "Privilege Escalation": [
        # Add C# privilege escalation vulnerable functions here
    ]
}

# PHP vulnerable functions
php_vulnerable_functions = {
    "Open Redirect": [
        "header(",
        "wp_redirect(",
        "wp_safe_redirect("
    ],
    "SQL Injection": [
        "->query_posts(",
        "->get_results(",
        "->query(",
        "->get_var(",
        "->get_row(",
        "->get_col(",
        "->replace(",
        "mysqli_query(",
        "mysqli_real_query(",
        "pg_query(",
        "pg_send_query(",
        "sqlite_open(",
        "sqlite_query(",
        "sqlite_exec(",
        "sqlite_single_query(",
        "->select("
    ],
    "Path Traversal": [
        "require(",
        "require_once(",
        "include(",
        "include_once(",
        "fread(",
        "unlink(",
        "readfile(",
        "file(",
        "file_get_contents(",
        "show_source(",
        "highlight_file("
    ],
    "Server-Side Request Forgery (SSRF)": [
        "file_get_contents(",
        "fopen(",
        "curl_init(",
        "curl_exec(",
        "curl_multi_exec",
        "curl_setopt(",
        "wp_remote_get(",
        "wp_remote_post("
    ],
    "Command Injection": [
        "eval(",
        "create_function(",
        "assert(",
        "file_put_contents(",
        "sanitize_file_name(",
        "php:#input",
        "system(",
        "exec(",
        "shell_exec(",
        "passthru(",
        "popen(",
        "proc_open(",
        "pcntl_exec("
    ],
    "Insecure Deserialization": [
        "unserialize(",
        "maybe_unserialize("
    ],
    "XML External Entity (XXE)": [
        "simplexml_load_string(",
        "SimpleXMLElement(",
        "DOMDocument::loadXML(",
        "DOMDocument::loadHTML(",
        "DOMDocument::loadHTMLFile(",
        "xml_parse(",
        "xml_parse_into_struct(",
        "xml_parser_create_ns(",
        "xml_parser_create(",
        "XMLWriter::writeElement(",
        "XMLWriter::startElement(",
        "XMLWriter::writeElementNS(",
        "XMLWriter::startElementNS(",
        "XMLWriter::writeDTDElement("
    ],
    "Cross-Site Scripting (XSS)": [
        "echo",
        "print",
        "printf",
        "the_content(",
        "the_excerpt(",
        "the_title(",
        "comment_text(",
        "bloginfo(",
        "wp_title(",
        "get_the_author(",
        "get_comment_author_link(",
        "get_header(",
        "get_footer(",
        "get_sidebar(",
        "document.write",
        "innerHTML"
    ],
    "Server-Side Template Injection (SSTI)": [
        "->render(",
        "view(",
        "->display(",
        "->execute(",
        "->draw(",
        "->get(",
        "Twig\\Environment",
        "Smarty()",
        "Mustache_Engine",
        "League\\Plates\\Engine",
        "\\Phalcon\\Mvc\\View()",
        "Latte\\Engine",
        "PHPTAL(",
        "RainTPL",
        "Savant3()",
        "Dwoo\\Core()"
    ],
    "Privilege Escalation": [
        "add_action( 'wp_ajax_nopriv_"
    ]
}



