### user interface

#install shiny package

shinyServer(
  pageWithSidebar(
    headerPanel("My First Shiny App"),
    
    sidebarPanel(
      selectInput("Distribution", "Pleae Select Disbribution Type",
                  choices = c("Normal", "Exponential")),
      sliderInput("sampleSize", "Please Select Sample Size: ",
                  min=100, max=5000, value=1000, step=100),
      conditionalPanel(condition="input.Distribution == 'Normal'",
                       textInput("mean", "Please Select The Mean", 10),
                       textInput("sd", "Please Select Standard Deviation", 3)),
      conditionalPanel(condition="input.Distribution == 'Exponent'ial",
                       textInput("lambda", "Please Select Exponential Lambda: ", 1))
    ),
    
    mainPanel(
      plotOutput("myPlot")
    )
    
  )  
  
)
