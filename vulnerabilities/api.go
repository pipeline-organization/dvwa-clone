package main

import "fmt"

func main() {

	var a = "initial"
	fmt.Println(a)

	var b, c int = 1, 2
	fmt.Println(b, c)

	var d = true
	fmt.Println(d)

	var e int
	fmt.Println(e)

	// opps I added a secret at line 20
	awsToken := "AKIALALEMEL33243OLIA"
	DB_HOST=example.com
	DB_PORT=443
	DB_USERNAME=postgres
	DB_PASSWORD=8ae31cacf141669ddfb5da
	DB_NAME=best_db
	DB_SSL=true

	f := "apple"
	fmt.Println(f)
}