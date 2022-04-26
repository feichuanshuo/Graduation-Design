import React, {Component} from 'react';
import {Card, Row, Col, Statistic, message} from "antd";
import { Liquid,Bullet } from '@ant-design/plots';
import "./index.less";
import BarChart from "../../../myComponents/barChart";
import SearchInput from "../../../myComponents/searchInput";
import {reqDetailData,reqSearchHint} from "../../../api";
import {SUCCESS_CODE} from "../../../config";

class DetailData extends Component {

    state = {
        detailData: {
            name : "",
            address : "",
            price : 0,
            estimated_price : 0.0,
            plotRatio : 0.0,
            greeningRate : 0,
            busStop : 0,
            subwayStations : 0,
            kindergarten : 0,
            primarySchool : 0,
            middleSchool : 0,
            hospital : 0,
            shoppingMall : 0,
            supermarket : 0,
            park : 0,
        },
    }

    searchInputRef = React.createRef();

    // 获取搜索提示
    getSearchHint = (keyword)=>{
        reqSearchHint(keyword).then((res)=>{
            const {code,msg,data} = res;
            if(code === SUCCESS_CODE) {
                this.searchInputRef.current.setSearchHint(data);
            }
            else{
                message.warn(msg)
            }
        }).catch((err)=>{
            console.log(err)
        })
    }


    // 获取小区详情
    getDetailData = (name)=>{
        reqDetailData(name).then((res)=>{
            const {code,msg,data} = res
            if(code === SUCCESS_CODE) {
                this.setState({
                    detailData: data
                })
            }
            else {
                message.warn(msg,1)
            }
        }).catch((err)=>{
            console.log(err)
        })
    }

    componentDidMount() {
        this.getDetailData("紫薇田园都市")
    }

    render() {
        const {detailData,searchHint} = this.state;
        const greeningRateConfig = {
            animation:true,
            height: 120,
            color: '#32CD32',
            outline: {
                border: 4,
                distance: 4,
            },
            wave: {
                length: 128,
            },
            liquidStyle: {
                fill: '#32CD32',
            }
        };
        const priceConfig = {
            data: [{
                title: '价格',
                ranges: [100000],
                reference_price: [detailData.price],
                estimated_price: detailData.estimated_price,
            }],
            height: 170,
            measureField: 'reference_price',
            rangeField: 'ranges',
            targetField: 'estimated_price',
            xField: 'title',
            color: {
                range: '#f0efff',
                measure: '#5B8FF9',
                target: '#FF3333 ',
            },
            xAxis: {
                line: null,
            },
            yAxis: false,
            label: {
                measure: {
                    position: 'middle',
                    style: {
                        fill: '#fff',
                    },
                },
                target: {
                    position: 'middle',
                },
            },
            // 自定义 legend
            legend: {
                custom: true,
                position: 'bottom',
                items: [
                    {
                        value: '政府参考价',
                        name: '政府参考价',
                        marker: {
                            symbol: 'square',
                            style: {
                                fill: '#5B8FF9',
                                r: 5,
                            },
                        },
                    },
                    {
                        value: '预估价',
                        name: '预估价',
                        marker: {
                            symbol: 'line',
                            style: {
                                stroke: '#FF3333 ',
                                r: 5,
                            },
                        },
                    },
                ],
            },

        }
        return (
            <div style = {{minHeight:'100%'}}>
                <Card
                    title = {"小区详情"}
                    className = {"data-card"}
                    extra = {<SearchInput
                        ref={this.searchInputRef}
                        onChange={(e)=>{
                            this.getSearchHint(e.target.value)
                        }}
                        searchHint={searchHint}
                    />}
                >
                    <Row gutter={[16,16]}>
                        <Col span={24}>
                            <Card>
                                <Statistic
                                    title="小区名称"
                                    value={detailData.name}
                                    precision={2}
                                    valueStyle={{textAlign:'center' }}
                                />
                            </Card>
                        </Col>
                        <Col span={12}>
                            <Card>
                                <Statistic
                                    title="政府参考单价"
                                    value={detailData.price}
                                    precision={2}
                                    valueStyle={{ color: '#3f8600',textAlign:'center' }}
                                    suffix="元/平方米"
                                    style={{height:'60px'}}
                                />
                            </Card>
                            <Card>
                                <Statistic
                                    title="预估价"
                                    value={detailData.estimated_price}
                                    precision={2}
                                    valueStyle={{ color: '#cf1322',textAlign:'center' }}
                                    suffix="元/平方米"
                                    style={{height:'60px'}}
                                />
                            </Card>
                        </Col>
                        <Col span={12}>
                            <Card>
                                <Bullet {...priceConfig} />
                            </Card>
                        </Col>
                        <Col span={24}>
                            <Card>
                                <Statistic
                                    title="小区位置"
                                    value={detailData.address}
                                    precision={2}
                                    valueStyle={{textAlign:'center' }}
                                />
                            </Card>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>硬件设施</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'容积率'} value={detailData.plotRatio} range={100} width={500} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.plotRatio}</h5>
                                </div>
                                <div>
                                    <Liquid {...greeningRateConfig}  percent={detailData.greeningRate/100} />
                                    <h1 style={{textAlign:'center'}}>绿化率</h1>
                                </div>
                            </div>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>交通配置</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'公交站数量'} value={detailData.busStop} range={30} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.busStop}</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'地铁站数量'} value={detailData.subwayStations} range={200} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.subwayStations}</h5>
                                </div>
                            </div>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>教育与医疗</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'幼儿园数量'} value={detailData.kindergarten} range={150} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.kindergarten}</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'小学数量　'} value={detailData.primarySchool} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.primarySchool}</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'中学数量　'} value={detailData.middleSchool} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.middleSchool}</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'医院数量　'} value={detailData.hospital} range={100} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.hospital}</h5>
                                </div>
                            </div>
                        </Col>
                        <Col span={12}>
                            <div className={"detail-card"} style={{height:'260px'}}>
                                <h1>购物与休闲</h1>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'购物中心'} value={detailData.shoppingMall} range={150} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.shoppingMall}</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'超市　　'} value={detailData.supermarket} range={2500} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.supermarket}</h5>
                                </div>
                                <div style={{display:"flex",lineHeight:'42px'}}>
                                    <BarChart tag={'公园　　'} value={detailData.park} range={50} width={450} height={20} color={'#178dfb'}/>
                                    <h5>{detailData.park}</h5>
                                </div>
                            </div>
                        </Col>
                    </Row>
                </Card>
            </div>

        );
    }
}

export default DetailData;
