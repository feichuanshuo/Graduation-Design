import React, {Component} from 'react';
import {Card, message, Table} from 'antd';
import { Mix } from '@ant-design/plots';

import {reqSupplyData} from "../../../api";
import {SUCCESS_CODE} from "../../../config";

//表格配置
const columns = [
    {
        title: '月份',
        dataIndex: 'time',
        key: 'time',
    },
    {
        title: '供应宗数(块)',
        dataIndex: 'supply_num',
        key: 'supply_num',
    },
    {
        title: '供应面积(㎡)',
        dataIndex: 'supply_area',
        key: 'supply_area',
    },
    {
        title: '供应均价(元/㎡) ',
        key: 'supply_price',
        dataIndex: 'supply_price',
    },
    {
        title: '楼面价(元/㎡) ',
        key: 'floor_price',
        dataIndex: 'floor_price'
    },
];

class SupplyData extends Component {

    state = {
        data:[],
        time_area:[],
        time_price:[]
    }

    getDataList = (len)=>{
        reqSupplyData(len).then((res)=>{
            const {data,code,msg}= res.data
            if(code===SUCCESS_CODE){
                let time_area = []
                let time_price = []
                data.forEach((item)=>{
                    time_area.push({
                        date:item.time,
                        value:parseFloat((item.supply_area/10000).toFixed(2)),
                    })
                    time_price.push({
                        dare:item.time,
                        value:item.supply_price
                    })
                })
                time_area=time_area.reverse()
                time_price=time_price.reverse()
                console.log(time_price)
                this.setState({
                    data,
                    time_area,
                    time_price
                })
            }
            else{
                message.error(msg,1)
            }
        }).catch((err)=>{
            console.log(err)
        })
    }

    componentDidMount() {
        this.getDataList(10)
    }

    render() {
        const {data,time_area,time_price} = this.state
        const config = {
            appendPadding: 8,
            tooltip: {
                shared: true,
            },
            syncViewPadding: true,
            plots: [
                {
                    type: 'column',
                    options: {
                        data:time_area,
                        xField: 'date',
                        yField: 'value',
                        yAxis: {
                            max: 400,
                        },
                        meta: {
                            date: {
                                sync: true,
                            },
                            value: {
                                alias: '供应面积(万㎡)',
                            },
                        },
                        label: {
                            position: 'middle',
                        },
                    },
                },
                {
                    type: 'line',
                    options: {
                        data: time_price,
                        xField: 'date',
                        yField: 'value',
                        xAxis: false,
                        yAxis: {
                            line: null,
                            grid: null,
                            position: 'right',
                            max: 20000,
                        },
                        meta: {
                            date: {
                                sync: 'date',
                            },
                            value: {
                                alias: '供应均价(元/㎡)',
                            },
                        },
                        smooth: true,
                        label: {
                            callback: (value) => {
                                return {
                                    offsetY: value,
                                    style: {
                                        fill: '#1AAF8B',
                                        fontWeight: 700,
                                        stroke: '#fff',
                                        lineWidth: 1,
                                    },
                                };
                            },
                        },
                        color: '#1AAF8B',
                    },
                },
            ],
        };
        return (
            <Card title={"供给数据"} className={"data-card"} bodyStyle={{height:'100%',backgroundColor:'whitesmoke',padding:0,borderTop:'solid whitesmoke'}}>
                <div className={"data-charts"}>
                    <Mix {...config} />
                </div>
                <div className={"data-table"}>
                    <Table columns={columns} dataSource={data} pagination={false}/>
                </div>
            </Card>
        );
    }
}

export default SupplyData;
