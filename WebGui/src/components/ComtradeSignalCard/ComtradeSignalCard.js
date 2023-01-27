function comtradeCard(props){
return(
<Card className="card-chart">
    <CardHeader>
    <h5 className="card-category">Total Shipments</h5>
    <CardTitle tag="h3">
        <i className="tim-icons icon-bell-55 text-info" /> 763,215
    </CardTitle>
    </CardHeader>
    <CardBody>
    <div className="chart-area">
        <Line
        data={chartExample2.data}
        options={chartExample2.options}
        />
    </div>
    </CardBody>
</Card>)
}