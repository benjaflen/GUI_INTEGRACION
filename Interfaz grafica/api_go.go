package main /* package main */

/*LIBRERIAS A UTILIZAR*/
import (
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

//VARIABLES
var j int
var duda bool

type instrumento struct {
	ID                 string `json:"id"`
	Nombre             string `json:"nombre"`
	Stock              int    `json:"stock"`
	Precio             int    `json:"precio"`
	Fecha_modificacion string `json:"fecha_modificacion"`
}

var instrumentos = []instrumento{
	{ID: "1", Nombre: "Batería electrónica Avatar SD61-6", Stock: 1, Precio: 500000, Fecha_modificacion: time.Now().String()},
	{ID: "2", Nombre: "guitarra", Stock: 30, Precio: 300000, Fecha_modificacion: time.Now().String()},
	{ID: "15", Nombre: "bajo", Stock: 10, Precio: 900000, Fecha_modificacion: time.Now().String()},
	{ID: "12", Nombre: "saxo", Stock: 30, Precio: 500000, Fecha_modificacion: time.Now().String()},
}

func getInstrumentos(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, instrumentos)
}

func getIns(c *gin.Context) {

	v_id := c.Param("id")
	for i := 0; i < len(instrumentos); i++ {
		if v_id == instrumentos[i].ID {
			j = i
			duda = true
		}

	}

	if duda == false {
		c.IndentedJSON(http.StatusOK, "no existe")
	}
	if duda == true {
		c.IndentedJSON(http.StatusOK, instrumentos[j])
	}
	duda = false
	j = -1

}
func main() { /* incio de funcion main*/
	router := gin.Default()
	router.GET("/instrumentos", getInstrumentos)

	router.GET("/instrumentos/:id", getIns)
	router.Run("localhost:8080")

}
