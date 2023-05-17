

using System;
using System.Net;
using System.Text.Json;

using var client = new HttpClient();


/*********** LOGIN **************/
var queryString = new System.Collections.Generic.Dictionary<string, string>()
   {
       { "username", "jenna" },
       { "pwd", "pwd" }
   };

var requestUrl = new UriBuilder("http://localhost:5000/api/users/login");
requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

var response = await client.GetAsync(requestUrl.ToString());
response.EnsureSuccessStatusCode();

var res = await response.Content.ReadAsStringAsync();
Console.WriteLine(res);



/*********** INSERT **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//    {
//        { "query", "'alfonzo', md5('pwd'), 'apikey', '0', 'email', 'full name'" },
//    };

//var requestUrl = new UriBuilder("http://localhost:5000/api/users/create");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);


/*********** UPDATE **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//    {

//        { "api_key", "not applicable" },
//        { "query", "SET username='bill' WHERE username='alfonzo'" }
//    };

//var requestUrl = new UriBuilder("http://localhost:5000/api/users/update");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);



/*********** DELETE **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//    {

//        { "api_key", "not applicable" },
//        { "query", "username='alfonzo'" }
//    };

//var requestUrl = new UriBuilder("http://localhost:5000/api/users/delete");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);




/*********** TICKER METRICS **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//{
//    { "api_key", "07f36a5b1c35e69f0046d0e6a3ab12d6" },
//    { "ticker", "MSFT" }
//};

//var requestUrl = new UriBuilder("http://localhost:5000/api/ticker/ticker_metrics");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);


/*********** SEC FILINGS **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//{
//    { "api_key", "07f36a5b1c35e69f0046d0e6a3ab12d6" },
//    { "ticker", "MSFT" }
//};

//var requestUrl = new UriBuilder("http://localhost:5000/api/ticker/sec_filings");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);


/*********** BALANCE SHEET **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//{
//    { "api_key", "07f36a5b1c35e69f0046d0e6a3ab12d6" },
//    { "ticker", "MSFT" }
//};

//var requestUrl = new UriBuilder("http://localhost:5000/api/ticker/balance_sheet");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);

/*********** CASH FLOW STATEMENT **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//{
//    { "api_key", "07f36a5b1c35e69f0046d0e6a3ab12d6" },
//    { "ticker", "MSFT" }
//};

//var requestUrl = new UriBuilder("http://localhost:5000/api/ticker/cash_flow_statement");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);

/*********** INCOME STATEMENT **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//{
//    { "api_key", "07f36a5b1c35e69f0046d0e6a3ab12d6" },
//    { "ticker", "MSFT" }
//};

//var requestUrl = new UriBuilder("http://localhost:5000/api/ticker/income_statement");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);


/*********** NEWS ARTICLES **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//{
//    { "api_key", "07f36a5b1c35e69f0046d0e6a3ab12d6" },
//};

//var requestUrl = new UriBuilder("http://localhost:5000/api/news");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var res = await response.Content.ReadAsStringAsync();
//Console.WriteLine(res);


/*********** DOWNLOAD INCOME STATEMENT **************/
//var queryString = new System.Collections.Generic.Dictionary<string, string>()
//{
//    { "api_key", "07f36a5b1c35e69f0046d0e6a3ab12d6" },
//    { "ticker", "MSFT" }
//};

//var requestUrl = new UriBuilder("http://localhost:5000/api/download/income_statement");
//requestUrl.Query = new System.Net.Http.FormUrlEncodedContent(queryString).ReadAsStringAsync().Result;

//var response = await client.GetAsync(requestUrl.ToString());
//response.EnsureSuccessStatusCode();

//var json = await response.Content.ReadAsStringAsync();
//var document = JsonDocument.Parse(json);
//var uri = document.RootElement.GetProperty("results").ToString();




//string ticker = "MSFT";
//string statementName = "income_statement";
//string apiKey = "2b1c52c776217c377aa030db56150115";
//string homeDir = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
//string filePath = Path.Combine(homeDir, "Downloads", $"{ticker}_{statementName}.csv");

//Dictionary<string, string> payload = new Dictionary<string, string>();
//payload["apikey"] = apiKey;

//WebClient cl = new WebClient();
//cl.QueryString = new System.Collections.Specialized.NameValueCollection();
//foreach (KeyValuePair<string, string> item in payload)
//{
//    cl.QueryString.Add(item.Key, item.Value);
//}

//string responseString = cl.DownloadString(uri);
//File.WriteAllText(filePath, responseString);

