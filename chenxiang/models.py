# -*- coding:UTF-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Accinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    comname = models.CharField(db_column='ComName', max_length=100)  # Field name made lowercase.
    addr = models.CharField(db_column='Addr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leaglman = models.CharField(db_column='LeaglMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxno = models.CharField(db_column='TaxNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankno = models.CharField(db_column='BankNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    currentyear = models.IntegerField(db_column='CurrentYear', blank=True, null=True)  # Field name made lowercase.
    currentmonth = models.IntegerField(db_column='CurrentMonth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccInfo'


class Accset(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accvalue = models.CharField(db_column='AccValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    controltype = models.IntegerField(db_column='ControlType', blank=True, null=True)  # Field name made lowercase.
    list = models.CharField(db_column='List', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccSet'


class Accountbill(models.Model):
    accountbillid = models.AutoField(db_column='AccountBillID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID')  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID')  # Field name made lowercase.
    dtlid = models.IntegerField(db_column='DtlID', blank=True, null=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    addamt = models.FloatField(db_column='AddAmt', blank=True, null=True)  # Field name made lowercase.
    minusamt = models.FloatField(db_column='MinusAmt', blank=True, null=True)  # Field name made lowercase.
    payamt = models.FloatField(db_column='PayAmt', blank=True, null=True)  # Field name made lowercase.
    eamt = models.FloatField(db_column='EAmt', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PaidAmt', blank=True, null=True)  # Field name made lowercase.
    oweamt = models.FloatField(db_column='OweAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountBill'


class Allbilldtl(models.Model):
    allbilldtlid = models.AutoField(db_column='AllBillDtlID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    dtlid = models.IntegerField(db_column='DtlID', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    inqty = models.FloatField(db_column='InQty', blank=True, null=True)  # Field name made lowercase.
    inprice = models.FloatField(db_column='InPrice', blank=True, null=True)  # Field name made lowercase.
    inamt = models.FloatField(db_column='InAmt', blank=True, null=True)  # Field name made lowercase.
    outqty = models.FloatField(db_column='OutQty', blank=True, null=True)  # Field name made lowercase.
    outprice = models.FloatField(db_column='OutPrice', blank=True, null=True)  # Field name made lowercase.
    outamt = models.FloatField(db_column='OutAmt', blank=True, null=True)  # Field name made lowercase.
    eqty = models.FloatField(db_column='EQty', blank=True, null=True)  # Field name made lowercase.
    eprice = models.FloatField(db_column='EPrice', blank=True, null=True)  # Field name made lowercase.
    eamt = models.FloatField(db_column='EAmt', blank=True, null=True)  # Field name made lowercase.
    selectflag = models.CharField(db_column='SelectFlag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    calculated = models.IntegerField(db_column='Calculated', blank=True, null=True)  # Field name made lowercase.
    purchaseqty = models.FloatField(db_column='PurchaseQty', blank=True, null=True)  # Field name made lowercase.
    purchaseamt = models.FloatField(db_column='PurchaseAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllBillDtl'


class Allbillfifo(models.Model):
    allbillfifoid = models.AutoField(db_column='AllBillFIFOID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    dtlid = models.IntegerField(db_column='DtlID', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    inqty = models.FloatField(db_column='InQty', blank=True, null=True)  # Field name made lowercase.
    inprice = models.FloatField(db_column='InPrice', blank=True, null=True)  # Field name made lowercase.
    inamt = models.FloatField(db_column='InAmt', blank=True, null=True)  # Field name made lowercase.
    outqty = models.FloatField(db_column='OutQty', blank=True, null=True)  # Field name made lowercase.
    outprice = models.FloatField(db_column='OutPrice', blank=True, null=True)  # Field name made lowercase.
    outamt = models.FloatField(db_column='OutAmt', blank=True, null=True)  # Field name made lowercase.
    eqty = models.FloatField(db_column='EQty', blank=True, null=True)  # Field name made lowercase.
    eprice = models.FloatField(db_column='EPrice', blank=True, null=True)  # Field name made lowercase.
    eamt = models.FloatField(db_column='EAmt', blank=True, null=True)  # Field name made lowercase.
    refqty = models.FloatField(db_column='RefQty', blank=True, null=True)  # Field name made lowercase.
    refamt = models.FloatField(db_column='RefAmt', blank=True, null=True)  # Field name made lowercase.
    refcount = models.IntegerField(db_column='RefCount', blank=True, null=True)  # Field name made lowercase.
    difamt = models.FloatField(db_column='DifAmt', blank=True, null=True)  # Field name made lowercase.
    calculated = models.IntegerField(db_column='Calculated', blank=True, null=True)  # Field name made lowercase.
    needupdatebill = models.IntegerField(db_column='NeedUpdateBill', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllBillFIFO'


class Allbillfiforef(models.Model):
    allbillfifoid = models.IntegerField(db_column='AllBillFIFOID', primary_key=True)  # Field name made lowercase.
    referallbillfifoid = models.IntegerField(db_column='ReferAllBillFIFOID')  # Field name made lowercase.
    refqty = models.FloatField(db_column='RefQty', blank=True, null=True)  # Field name made lowercase.
    refamt = models.FloatField(db_column='RefAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllBillFIFORef'
        unique_together = (('allbillfifoid', 'referallbillfifoid'),)


class Area(models.Model):
    areaid = models.IntegerField(db_column='AreaID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area'


class Bank(models.Model):
    bankid = models.IntegerField(db_column='BankID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    initamt = models.FloatField(db_column='InitAmt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bank'


class Bankbill(models.Model):
    bankbillid = models.AutoField(db_column='BankBillID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID')  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID')  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID')  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addamt = models.FloatField(db_column='AddAmt', blank=True, null=True)  # Field name made lowercase.
    minusamt = models.FloatField(db_column='MinusAmt', blank=True, null=True)  # Field name made lowercase.
    eamt = models.FloatField(db_column='EAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankBill'


class Base(models.Model):
    windowid = models.IntegerField(db_column='WindowID', primary_key=True)  # Field name made lowercase.
    sqlstr = models.CharField(db_column='SqlStr', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Base'


class Billselect(models.Model):
    billselectid = models.IntegerField(db_column='BillSelectID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    selectedwindowid = models.IntegerField(db_column='SelectedWindowID', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    procname = models.CharField(db_column='ProcName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    keyfield = models.CharField(db_column='KeyField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uniquefield = models.CharField(db_column='UniqueField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uniqueerrmsg = models.CharField(db_column='UniqueErrMsg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scheckfields = models.CharField(db_column='SCheckFields', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    dcheckfields = models.CharField(db_column='DCheckFields', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    lcblistsql = models.CharField(db_column='lcbListSql', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    columnset = models.CharField(db_column='ColumnSet', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    datasetcount = models.IntegerField(db_column='DataSetCount', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    dtlindexfieldnames = models.CharField(db_column='DtlIndexFieldNames', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillSelect'


class Billselectdtl(models.Model):
    billselectdtlid = models.AutoField(db_column='BillSelectDtlID', primary_key=True)  # Field name made lowercase.
    billselectid = models.IntegerField(db_column='BillSelectID', blank=True, null=True)  # Field name made lowercase.
    tabletype = models.IntegerField(db_column='TableType', blank=True, null=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    writetype = models.IntegerField(db_column='WriteType', blank=True, null=True)  # Field name made lowercase.
    writefield = models.CharField(db_column='WriteField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    footervaluetype = models.IntegerField(db_column='FooterValueType', blank=True, null=True)  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.
    israte = models.IntegerField(db_column='IsRate', blank=True, null=True)  # Field name made lowercase.
    iscurrency = models.IntegerField(db_column='IsCurrency', blank=True, null=True)  # Field name made lowercase.
    disableonchange = models.IntegerField(db_column='DisableOnchange', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillSelectDtl'


class Bom(models.Model):
    bomid = models.IntegerField(db_column='BomID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    finishedgoodsid = models.IntegerField(db_column='FinishedGoodsID', blank=True, null=True)  # Field name made lowercase.
    finishedgoodsqty = models.FloatField(db_column='FinishedGoodsQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bom'


class Bomdtl(models.Model):
    bomdtlid = models.AutoField(db_column='BomDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    bomid = models.IntegerField(db_column='BomID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    wasteqty = models.FloatField(db_column='WasteQty', blank=True, null=True)  # Field name made lowercase.
    wasterate = models.FloatField(db_column='WasteRate', blank=True, null=True)  # Field name made lowercase.
    requiredqty = models.FloatField(db_column='RequiredQty', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BomDtl'


class Bucha(models.Model):
    buchaid = models.IntegerField(db_column='BuChaID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    goodsseriesid = models.IntegerField(db_column='GoodsSeriesID', blank=True, null=True)  # Field name made lowercase.
    channelid = models.IntegerField(db_column='ChannelID', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BuCha'


class Buchadtl(models.Model):
    buchadtlid = models.AutoField(db_column='BuChaDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    buchaid = models.IntegerField(db_column='BuChaID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    oldprice = models.FloatField(db_column='OldPrice', blank=True, null=True)  # Field name made lowercase.
    newprice = models.FloatField(db_column='NewPrice', blank=True, null=True)  # Field name made lowercase.
    diffprice = models.FloatField(db_column='DiffPrice', blank=True, null=True)  # Field name made lowercase.
    diffamt = models.FloatField(db_column='DiffAmt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BuChaDtl'


class Chajia(models.Model):
    chajiaid = models.IntegerField(db_column='ChaJiaID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.ForeignKey('Client',db_column='ClientID',null=True,blank=True)  # Field name made lowercase.
    clienttypeid = models.IntegerField(db_column='ClientTypeID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChaJia'


class Chajiadtl(models.Model):
    chajiadtlid = models.AutoField(db_column='ChaJiaDtlID', primary_key=True)  # Field name made lowercase.
    chajiaid = models.IntegerField(db_column='ChaJiaID', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    saleid = models.IntegerField(db_column='SaleID', blank=True, null=True)  # Field name made lowercase.
    saleprice = models.FloatField(db_column='SalePrice', blank=True, null=True)  # Field name made lowercase.
    jiesuanprice = models.FloatField(db_column='JieSuanPrice', blank=True, null=True)  # Field name made lowercase.
    diffprice = models.FloatField(db_column='DiffPrice', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChaJiaDtl'


class Channel(models.Model):
    channelid = models.IntegerField(db_column='ChannelID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Channel'


class Charge(models.Model):
    chargeid = models.IntegerField(db_column='ChargeID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    factamt = models.FloatField(db_column='FactAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Charge'


class Chargedtl(models.Model):
    chargedtlid = models.AutoField(db_column='ChargeDtlID', primary_key=True)  # Field name made lowercase.
    chargeid = models.IntegerField(db_column='ChargeID')  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChargeDtl'


class Chargeoff(models.Model):
    chargeoffid = models.IntegerField(db_column='ChargeOffID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    chargeofftypeid = models.IntegerField(db_column='ChargeOffTypeID', blank=True, null=True)  # Field name made lowercase.
    clientid1 = models.IntegerField(db_column='ClientID1')  # Field name made lowercase.
    clientid2 = models.IntegerField(db_column='ClientID2', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChargeOff'


class Chargeoffdtl(models.Model):
    chargeoffdtlid = models.AutoField(db_column='ChargeOffDtlID', primary_key=True)  # Field name made lowercase.
    chargeoffid = models.IntegerField(db_column='ChargeOffID')  # Field name made lowercase.
    item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChargeOffDtl'


class Chargeofftype(models.Model):
    chargeofftypeid = models.IntegerField(db_column='ChargeOffTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    client1lookupdatasetid = models.IntegerField(db_column='Client1LookupDataSetID', blank=True, null=True)  # Field name made lowercase.
    client1caption = models.CharField(db_column='Client1Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    client1listfield = models.CharField(db_column='Client1ListField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tabsheet1caption = models.CharField(db_column='TabSheet1Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billselect1 = models.IntegerField(db_column='BillSelect1', blank=True, null=True)  # Field name made lowercase.
    client2lookupdatasetid = models.IntegerField(db_column='Client2LookupDataSetID', blank=True, null=True)  # Field name made lowercase.
    client2caption = models.CharField(db_column='Client2Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    client2listfield = models.CharField(db_column='Client2ListField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tabsheet2caption = models.CharField(db_column='TabSheet2Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billselect2 = models.IntegerField(db_column='BillSelect2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChargeOffType'


class Client(models.Model):
    clientid = models.IntegerField(db_column='ClientID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneID', blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    channelid = models.IntegerField(db_column='ChannelID', blank=True, null=True)  # Field name made lowercase.
    clientlevid = models.IntegerField(db_column='ClientLevID', blank=True, null=True)  # Field name made lowercase.
    clienttypeid = models.IntegerField(db_column='ClientTypeID', blank=True, null=True)  # Field name made lowercase.
    clienttype = models.IntegerField(db_column='ClientType', blank=True, null=True)  # Field name made lowercase.
    isdouble = models.IntegerField(db_column='IsDouble', blank=True, null=True)  # Field name made lowercase.
    clientstateid = models.IntegerField(db_column='ClientStateID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    kefuid = models.IntegerField(db_column='KeFuID', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    assistcode = models.CharField(db_column='AssistCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.FloatField(db_column='CreditAmt', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    init = models.FloatField(db_column='Init', blank=True, null=True)  # Field name made lowercase.
    daysofpayment = models.IntegerField(db_column='DaysOfPayment', blank=True, null=True)  # Field name made lowercase.
    modeofpayment = models.CharField(db_column='ModeOfPayment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ismanufacture = models.IntegerField(db_column='IsManufacture', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    legalrep = models.CharField(db_column='LegalRep', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxid = models.CharField(db_column='TaxID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    msn = models.CharField(db_column='MSN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taobao = models.CharField(db_column='TaoBao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'

    def __str__(self):
        return self.name


class Clientlev(models.Model):
    clientlevid = models.IntegerField(db_column='ClientLevID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientLev'


class Clientstate(models.Model):
    clientstateid = models.IntegerField(db_column='ClientStateID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientState'


class Clienttype(models.Model):
    clienttypeid = models.IntegerField(db_column='ClientTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientType'


class Columnset(models.Model):
    columnsetid = models.IntegerField(db_column='ColumnSetID')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', primary_key=True)  # Field name made lowercase.
    tablefieldid = models.IntegerField(db_column='TableFieldID')  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colvisible = models.IntegerField(db_column='ColVisible', blank=True, null=True)  # Field name made lowercase.
    colfixed = models.IntegerField(db_column='ColFixed', blank=True, null=True)  # Field name made lowercase.
    colwidth = models.IntegerField(db_column='ColWidth', blank=True, null=True)  # Field name made lowercase.
    ctrlvisible = models.IntegerField(db_column='CtrlVisible', blank=True, null=True)  # Field name made lowercase.
    ctrlfixed = models.IntegerField(db_column='CtrlFixed', blank=True, null=True)  # Field name made lowercase.
    ctrlwidth = models.IntegerField(db_column='CtrlWidth', blank=True, null=True)  # Field name made lowercase.
    searchmode = models.IntegerField(db_column='SearchMode', blank=True, null=True)  # Field name made lowercase.
    autodropdown = models.IntegerField(db_column='AutoDropDown', blank=True, null=True)  # Field name made lowercase.
    readonly = models.IntegerField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.
    tag = models.IntegerField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autocopy = models.IntegerField(db_column='AutoCopy', blank=True, null=True)  # Field name made lowercase.
    dropdownrows = models.IntegerField(db_column='DropDownRows', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ColumnSet'
        unique_together = (('operatorid', 'tablefieldid'),)


class Columnsets(models.Model):
    columnsetsid = models.AutoField(db_column='ColumnSetsID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    columnset = models.TextField(db_column='ColumnSet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ColumnSets'


class Customfield(models.Model):
    customfieldid = models.AutoField(db_column='CustomFieldID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    lookupdatasetid = models.IntegerField(db_column='LookupDataSetID', blank=True, null=True)  # Field name made lowercase.
    list = models.CharField(db_column='List', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomField'


class Datatype(models.Model):
    datatypeid = models.IntegerField(db_column='DataTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataType'


class Datetype(models.Model):
    datetypeid = models.IntegerField(db_column='DateTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DateType'


class Delivery(models.Model):
    deliveryid = models.IntegerField(db_column='DeliveryID', primary_key=True)  # Field name made lowercase.
    shopid = models.ForeignKey('Shop',db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='ReCheckID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    truckid = models.IntegerField(db_column='TruckID', blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    siji = models.IntegerField(db_column='SiJi', blank=True, null=True)  # Field name made lowercase.
    genche = models.IntegerField(db_column='GenChe', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='ReCheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    invalid = models.IntegerField(db_column='Invalid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Delivery'


class Deliverydtl(models.Model):
    deliverydtlid = models.AutoField(db_column='DeliveryDtlID', primary_key=True)  # Field name made lowercase.
    deliveryid = models.ForeignKey('Delivery',db_column='DeliveryID', blank=True, null=True)  # Field name made lowercase.
    codeinput = models.CharField(db_column='CodeInput', max_length=50, blank=True, null=True)  # Field name made lowercase.
    saleid = models.IntegerField(db_column='SaleID', blank=True, null=True)  # Field name made lowercase.
    pcs = models.FloatField(db_column='Pcs', blank=True, null=True)  # Field name made lowercase.
    pifajianshu = models.FloatField(db_column='PiFaJianShu', blank=True, null=True)  # Field name made lowercase.
    dest = models.CharField(db_column='Dest', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dianhuotime = models.CharField(db_column='DianHuoTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    likaitime = models.CharField(db_column='LiKaiTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeliveryDtl'


class Dept(models.Model):
    deptid = models.IntegerField(db_column='DeptID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dept'


class Emp(models.Model):
    empid = models.IntegerField(db_column='EmpID', primary_key=True)  # Field name made lowercase.
    sexid = models.IntegerField(db_column='SexID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    basewage = models.FloatField(db_column='BaseWage', blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='IDNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='BirthDay', blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iscountworker = models.IntegerField(db_column='IsCountWorker', blank=True, null=True)  # Field name made lowercase.
    issalesman = models.IntegerField(db_column='IsSalesMan', blank=True, null=True)  # Field name made lowercase.
    ischeckor = models.IntegerField(db_column='IsCheckor', blank=True, null=True)  # Field name made lowercase.
    isworker = models.IntegerField(db_column='IsWorker', blank=True, null=True)  # Field name made lowercase.
    isdriver = models.IntegerField(db_column='IsDriver', blank=True, null=True)  # Field name made lowercase.
    iscashier = models.IntegerField(db_column='IsCashier', blank=True, null=True)  # Field name made lowercase.
    isgenche = models.IntegerField(db_column='IsGenChe', blank=True, null=True)  # Field name made lowercase.
    iszhuangche = models.IntegerField(db_column='IsZhuangChe', blank=True, null=True)  # Field name made lowercase.
    istongji = models.IntegerField(db_column='IsTongJi', blank=True, null=True)  # Field name made lowercase.
    iszhuguan = models.IntegerField(db_column='IsZhuGuan', blank=True, null=True)  # Field name made lowercase.
    ischangzhang = models.IntegerField(db_column='IsChangZhang', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Emp'


class Errormsg(models.Model):
    error = models.IntegerField(db_column='Error', primary_key=True)  # Field name made lowercase.
    msg = models.CharField(db_column='Msg', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ErrorMsg'


class Exceptions(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    msg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Exceptions'


class Fee(models.Model):
    feeid = models.IntegerField(db_column='FeeID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fee'


class Feedtl(models.Model):
    feedtlid = models.AutoField(db_column='FeeDtlID', primary_key=True)  # Field name made lowercase.
    feeid = models.IntegerField(db_column='FeeID', blank=True, null=True)  # Field name made lowercase.
    feetypeid = models.IntegerField(db_column='FeeTypeID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeeDtl'


class Feetype(models.Model):
    feetypeid = models.IntegerField(db_column='FeeTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeeType'


class Feiyong(models.Model):
    feiyongid = models.IntegerField(db_column='FeiYongID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    clienttypeid = models.IntegerField(db_column='ClientTypeID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeiYong'


class Feiyongdtl(models.Model):
    feiyongdtlid = models.AutoField(db_column='FeiYongDtlID', primary_key=True)  # Field name made lowercase.
    feiyongid = models.IntegerField(db_column='FeiYongID', blank=True, null=True)  # Field name made lowercase.
    xiangmu = models.CharField(db_column='XiangMu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mingxi = models.CharField(db_column='MingXi', max_length=100, blank=True, null=True)  # Field name made lowercase.
    goodsseriesid = models.IntegerField(db_column='GoodsSeriesID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeiYongDtl'


class Filter(models.Model):
    filterid = models.IntegerField(db_column='FilterID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    datefilter = models.IntegerField(db_column='DateFilter', blank=True, null=True)  # Field name made lowercase.
    datevalue = models.CharField(db_column='DateValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shopfiltervalue = models.IntegerField(db_column='ShopFilterValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Filter'


class Filterdtl(models.Model):
    filterdtlid = models.IntegerField(db_column='FilterDtlID', primary_key=True)  # Field name made lowercase.
    filterid = models.IntegerField(db_column='FilterID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    filteritemid = models.IntegerField(db_column='FilterItemID', blank=True, null=True)  # Field name made lowercase.
    filteroperatedtlid = models.IntegerField(db_column='FilterOperateDtlID', blank=True, null=True)  # Field name made lowercase.
    operate = models.CharField(db_column='Operate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filtervalue = models.CharField(db_column='FilterValue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rightsid = models.IntegerField(db_column='RightsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FilterDtl'


class Filteritem(models.Model):
    filteritemid = models.IntegerField(db_column='FilterItemID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datafield = models.CharField(db_column='DataField', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType', blank=True, null=True)  # Field name made lowercase.
    filteroperateid = models.IntegerField(db_column='FilterOperateID', blank=True, null=True)  # Field name made lowercase.
    ctrltype = models.IntegerField(db_column='CtrlType', blank=True, null=True)  # Field name made lowercase.
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FilterItem'


class Filteroperate(models.Model):
    filteroperateid = models.IntegerField(db_column='FilterOperateID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FilterOperate'


class Filteroperatedtl(models.Model):
    filteroperatedtlid = models.AutoField(db_column='FilterOperateDtlID', primary_key=True)  # Field name made lowercase.
    filteroperateid = models.IntegerField(db_column='FilterOperateID', blank=True, null=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50)  # Field name made lowercase.
    operate = models.CharField(db_column='Operate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operateleft = models.CharField(db_column='OperateLeft', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operateright = models.CharField(db_column='OperateRight', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isdefault = models.IntegerField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    allowinput = models.IntegerField(db_column='AllowInput', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FilterOperateDtl'


class Forms(models.Model):
    formid = models.AutoField(db_column='FormID', primary_key=True)  # Field name made lowercase.
    moduleid = models.IntegerField(db_column='ModuleID', blank=True, null=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    righttype = models.CharField(db_column='RightType', max_length=12, blank=True, null=True)  # Field name made lowercase.
    fixedcols = models.IntegerField(db_column='FixedCols', blank=True, null=True)  # Field name made lowercase.
    formcaption = models.CharField(db_column='FormCaption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    captionwidth = models.IntegerField(db_column='CaptionWidth', blank=True, null=True)  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formwidth = models.IntegerField(db_column='FormWidth', blank=True, null=True)  # Field name made lowercase.
    billtype = models.CharField(db_column='BillType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    surcode = models.CharField(db_column='SurCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sepa = models.CharField(db_column='Sepa', max_length=32, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyfield = models.CharField(db_column='KeyField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dtltablename = models.CharField(db_column='DtlTableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    filter = models.CharField(db_column='Filter', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    orderby = models.CharField(db_column='OrderBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shopfilter = models.IntegerField(db_column='ShopFilter', blank=True, null=True)  # Field name made lowercase.
    datefilter = models.IntegerField(db_column='DateFilter', blank=True, null=True)  # Field name made lowercase.
    autocreate = models.IntegerField(db_column='AutoCreate', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    closedsign = models.IntegerField(db_column='ClosedSign', blank=True, null=True)  # Field name made lowercase.
    visiblebutton = models.CharField(db_column='VisibleButton', max_length=6, blank=True, null=True)  # Field name made lowercase.
    iscustomreport = models.IntegerField(db_column='IsCustomReport', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Forms'


class Goods(models.Model):
    goodsid = models.IntegerField(db_column='GoodsID', primary_key=True)  # Field name made lowercase.
    goodstypeid = models.IntegerField(db_column='GoodsTypeID', blank=True, null=True)  # Field name made lowercase.
    goodsseriesid = models.IntegerField(db_column='GoodsSeriesID', blank=True, null=True)  # Field name made lowercase.
    webclassid = models.IntegerField(db_column='WebClassID', blank=True, null=True)  # Field name made lowercase.
    websn = models.IntegerField(db_column='WebSn', blank=True, null=True)  # Field name made lowercase.
    goodskindid = models.IntegerField(db_column='GoodsKindID', blank=True, null=True)  # Field name made lowercase.
    goodscostingid = models.IntegerField(db_column='GoodsCostingID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.ForeignKey(to='Client',db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    vendorid = models.IntegerField(db_column='VendorID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    fcode = models.CharField(db_column='FCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistcode = models.CharField(db_column='AssistCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    istaobao = models.IntegerField(db_column='IsTaoBao', blank=True, null=True)  # Field name made lowercase.
    taobaoname = models.CharField(db_column='TaoBaoName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistunit = models.CharField(db_column='AssistUnit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    assistrate = models.FloatField(db_column='AssistRate', blank=True, null=True)  # Field name made lowercase.
    aprice = models.FloatField(db_column='APrice', blank=True, null=True)  # Field name made lowercase.
    validdates = models.IntegerField(db_column='ValidDates', blank=True, null=True)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cubage = models.FloatField(db_column='Cubage', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    factory = models.CharField(db_column='Factory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    onhand = models.FloatField(db_column='Onhand', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    topqty = models.FloatField(db_column='TopQty', blank=True, null=True)  # Field name made lowercase.
    floorqty = models.FloatField(db_column='FloorQty', blank=True, null=True)  # Field name made lowercase.
    pic = models.TextField(db_column='Pic', blank=True, null=True)  # Field name made lowercase.
    onlineintroduce = models.CharField(db_column='OnlineIntroduce', max_length=100, blank=True, null=True)  # Field name made lowercase.
    onlineprice = models.FloatField(db_column='OnLinePrice', blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=50, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=100, blank=True, null=True)  # Field name made lowercase.
    goodswebstateid = models.IntegerField(db_column='GoodsWebStateID', blank=True, null=True)  # Field name made lowercase.
    needcalc = models.IntegerField(db_column='NeedCalc', blank=True, null=True)  # Field name made lowercase.
    adddate = models.DateTimeField(db_column='AddDate', blank=True, null=True)  # Field name made lowercase.
    price1 = models.FloatField(db_column='Price1', blank=True, null=True)  # Field name made lowercase.
    price2 = models.FloatField(db_column='Price2', blank=True, null=True)  # Field name made lowercase.
    price3 = models.FloatField(db_column='Price3', blank=True, null=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='ChangeDate', blank=True, null=True)  # Field name made lowercase.
    syncdate = models.DateTimeField(db_column='SyncDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Goods'

    def __str__(self):
        return self.name


class Goodsclose(models.Model):
    goodscloseid = models.IntegerField(db_column='GoodsCloseID', primary_key=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsClose'


class Goodscosting(models.Model):
    goodscostingid = models.IntegerField(db_column='GoodsCostingID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsCosting'


class Goodsin(models.Model):
    goodsinid = models.IntegerField(db_column='GoodsInID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsIn'


class Goodsindtl(models.Model):
    goodsindtlid = models.AutoField(db_column='GoodsInDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    goodsinid = models.IntegerField(db_column='GoodsInID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsInDtl'


class Goodskind(models.Model):
    goodskindid = models.IntegerField(db_column='GoodsKindID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsKind'


class Goodslev(models.Model):
    goodslevid = models.IntegerField(db_column='GoodsLevID', primary_key=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID')  # Field name made lowercase.
    clientlevid = models.IntegerField(db_column='ClientLevID')  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsLev'


class Goodsloss(models.Model):
    goodslossid = models.IntegerField(db_column='GoodsLossID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsLoss'


class Goodslossdtl(models.Model):
    goodslossdtlid = models.AutoField(db_column='GoodsLossDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    goodslossid = models.IntegerField(db_column='GoodsLossID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsLossDtl'


class Goodsmonthdata(models.Model):
    accyear = models.IntegerField(db_column='AccYear', primary_key=True)  # Field name made lowercase.
    accmonth = models.IntegerField(db_column='AccMonth')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID')  # Field name made lowercase.
    aprice = models.FloatField(db_column='Aprice', blank=True, null=True)  # Field name made lowercase.
    onhand = models.FloatField(db_column='Onhand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsMonthData'
        unique_together = (('accyear', 'accmonth', 'goodsid'),)


class Goodsout(models.Model):
    goodsoutid = models.IntegerField(db_column='GoodsOutID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsOut'


class Goodsoutdtl(models.Model):
    goodsoutdtlid = models.AutoField(db_column='GoodsOutDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    goodsoutid = models.IntegerField(db_column='GoodsOutID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsOutDtl'


class Goodsseries(models.Model):
    goodsseriesid = models.IntegerField(db_column='GoodsSeriesID', primary_key=True)  # Field name made lowercase.
    sn = models.CharField(db_column='Sn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    abtype = models.CharField(db_column='ABType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    huowei = models.CharField(db_column='HuoWei', max_length=20, blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsSeries'


class Goodstype(models.Model):
    goodstypeid = models.IntegerField(db_column='GoodsTypeID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsType'


class Goodsunit(models.Model):
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', primary_key=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID')  # Field name made lowercase.
    unittypeid = models.IntegerField(db_column='UnitTypeID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    pprice = models.FloatField(db_column='PPrice', blank=True, null=True)  # Field name made lowercase.
    sprice = models.FloatField(db_column='SPrice', blank=True, null=True)  # Field name made lowercase.
    maxpprice = models.FloatField(db_column='MaxPPrice', blank=True, null=True)  # Field name made lowercase.
    minsprice = models.FloatField(db_column='MinSPrice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsUnit'


class Goodsworkpro(models.Model):
    goodsworkproid = models.IntegerField(db_column='GoodsWorkProID', primary_key=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    workproid = models.IntegerField(db_column='WorkProID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsWorkPro'


class Income(models.Model):
    incomeid = models.IntegerField(db_column='IncomeID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Income'


class Incomedtl(models.Model):
    incomedtlid = models.AutoField(db_column='IncomeDtlID', primary_key=True)  # Field name made lowercase.
    incomeid = models.IntegerField(db_column='IncomeID', blank=True, null=True)  # Field name made lowercase.
    incometypeid = models.IntegerField(db_column='IncomeTypeID', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IncomeDtl'


class Incometype(models.Model):
    incometypeid = models.IntegerField(db_column='IncomeTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IncomeType'


class Inventory(models.Model):
    inventoryid = models.IntegerField(db_column='InventoryID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventory'


class Inventorydtl(models.Model):
    inventorydtlid = models.AutoField(db_column='InventoryDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    inventoryid = models.IntegerField(db_column='InventoryID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    storeqty = models.FloatField(db_column='StoreQty', blank=True, null=True)  # Field name made lowercase.
    factqty = models.FloatField(db_column='FactQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryDtl'


class Jiesuan(models.Model):
    jiesuanid = models.IntegerField(db_column='JieSuanID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    clienttypeid = models.IntegerField(db_column='ClientTypeID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JieSuan'


class Jiesuandtl(models.Model):
    jiesuandtlid = models.AutoField(db_column='JieSuanDtlID', primary_key=True)  # Field name made lowercase.
    jiesuanid = models.IntegerField(db_column='JieSuanID')  # Field name made lowercase.
    saleid = models.IntegerField(db_column='SaleID', blank=True, null=True)  # Field name made lowercase.
    feiyongid = models.IntegerField(db_column='FeiYongID', blank=True, null=True)  # Field name made lowercase.
    feiyongamt = models.FloatField(db_column='FeiYongAmt', blank=True, null=True)  # Field name made lowercase.
    chajiaid = models.IntegerField(db_column='ChaJiaID', blank=True, null=True)  # Field name made lowercase.
    chajiaamt = models.FloatField(db_column='ChaJiaAmt', blank=True, null=True)  # Field name made lowercase.
    ladanid = models.IntegerField(db_column='LaDanID', blank=True, null=True)  # Field name made lowercase.
    ladanamt = models.FloatField(db_column='LaDanAmt', blank=True, null=True)  # Field name made lowercase.
    paytype = models.CharField(db_column='PayType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    molingamt = models.FloatField(db_column='MoLingAmt', blank=True, null=True)  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JieSuanDtl'


class Keyvaluetable(models.Model):
    tablename = models.CharField(db_column='TableName', primary_key=True, max_length=100)  # Field name made lowercase.
    keyvalue = models.IntegerField(db_column='Keyvalue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeyValueTable'


class Ladan(models.Model):
    ladanid = models.IntegerField(db_column='LaDanID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    clienttypeid = models.IntegerField(db_column='ClientTypeID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LaDan'


class Ladandtl(models.Model):
    ladandtlid = models.AutoField(db_column='LaDanDtlID', primary_key=True)  # Field name made lowercase.
    ladanid = models.IntegerField(db_column='LaDanID', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    saleid = models.IntegerField(db_column='SaleID', blank=True, null=True)  # Field name made lowercase.
    saleprice = models.FloatField(db_column='SalePrice', blank=True, null=True)  # Field name made lowercase.
    jiesuanprice = models.FloatField(db_column='JieSuanPrice', blank=True, null=True)  # Field name made lowercase.
    diffprice = models.FloatField(db_column='DiffPrice', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LaDanDtl'


class Line(models.Model):
    lineid = models.IntegerField(db_column='LineID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Line'


class Logininfo(models.Model):
    logininfoid = models.IntegerField(db_column='LoginInfoID', primary_key=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID')  # Field name made lowercase.
    logindate = models.DateTimeField(db_column='LoginDate', blank=True, null=True)  # Field name made lowercase.
    logoutdate = models.DateTimeField(db_column='LogoutDate', blank=True, null=True)  # Field name made lowercase.
    lastactivity = models.DateTimeField(db_column='LastActivity', blank=True, null=True)  # Field name made lowercase.
    online = models.IntegerField(db_column='Online', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoginInfo'


class Lookupdataset(models.Model):
    lookupdatasetid = models.IntegerField(db_column='LookupDataSetID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    datasetname = models.CharField(db_column='DataSetName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    selectstr = models.CharField(db_column='SelectStr', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    wherestr = models.CharField(db_column='WhereStr', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookupDataSet'


class Lookupfield(models.Model):
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', primary_key=True)  # Field name made lowercase.
    keyfields = models.CharField(db_column='KeyFields', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lookupdatasetid = models.IntegerField(db_column='LookupDataSetID', blank=True, null=True)  # Field name made lowercase.
    lookupkeyfields = models.CharField(db_column='LookupKeyFields', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lookupresultfield = models.CharField(db_column='LookupResultField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    listfilter = models.CharField(db_column='ListFilter', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    dropdownfilter = models.CharField(db_column='DropDownFilter', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    listkeyfield = models.CharField(db_column='ListKeyField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    listfield = models.CharField(db_column='ListField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    listfieldindex = models.IntegerField(db_column='ListFieldIndex', blank=True, null=True)  # Field name made lowercase.
    searchmode = models.IntegerField(db_column='SearchMode', blank=True, null=True)  # Field name made lowercase.
    visiblebutton = models.CharField(db_column='VisibleButton', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dropdownwidth = models.IntegerField(db_column='DropDownWidth', blank=True, null=True)  # Field name made lowercase.
    dropdownrows = models.IntegerField(db_column='DropDownRows', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookupField'


class MFinished(models.Model):
    m_finishedid = models.IntegerField(db_column='M_FinishedID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_Finished'


class MFinisheddtl(models.Model):
    m_finisheddtlid = models.AutoField(db_column='M_FinishedDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    m_finishedid = models.IntegerField(db_column='M_FinishedID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_FinishedDtl'


class MMaterial(models.Model):
    m_materialid = models.IntegerField(db_column='M_MaterialID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_Material'


class MMaterialdtl(models.Model):
    m_materialdtlid = models.AutoField(db_column='M_MaterialDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    m_materialid = models.IntegerField(db_column='M_MaterialID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    calculated = models.IntegerField(db_column='Calculated', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_MaterialDtl'


class MMaterialrtn(models.Model):
    m_materialrtnid = models.IntegerField(db_column='M_MaterialRtnID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_MaterialRtn'


class MMaterialrtndtl(models.Model):
    m_materialrtndtlid = models.AutoField(db_column='M_MaterialRtnDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    m_materialrtnid = models.IntegerField(db_column='M_MaterialRtnID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_MaterialRtnDtl'


class MPacking(models.Model):
    m_packingid = models.IntegerField(db_column='M_PackingID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    autosetbom = models.IntegerField(db_column='AutoSetBom', blank=True, null=True)  # Field name made lowercase.
    sumwl = models.IntegerField(db_column='SumWL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_Packing'


class MPackingdtl(models.Model):
    m_packingdtlid = models.AutoField(db_column='M_PackingDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    m_packingid = models.IntegerField(db_column='M_PackingID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    bomid = models.IntegerField(db_column='BomID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_PackingDtl'


class MPackingwl(models.Model):
    m_packingwlid = models.AutoField(db_column='M_PackingWLID', primary_key=True)  # Field name made lowercase.
    m_packingid = models.IntegerField(db_column='M_PackingID')  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bomid = models.IntegerField(db_column='BomID', blank=True, null=True)  # Field name made lowercase.
    m_packingdtlid = models.IntegerField(db_column='M_PackingDtlID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_PackingWL'


class MUnpacking(models.Model):
    m_unpackingid = models.IntegerField(db_column='M_UnPackingID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    autosetbom = models.IntegerField(db_column='AutoSetBom', blank=True, null=True)  # Field name made lowercase.
    sumwl = models.IntegerField(db_column='SumWL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_UnPacking'


class MUnpackingdtl(models.Model):
    m_unpackingdtlid = models.AutoField(db_column='M_UnPackingDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    m_unpackingid = models.IntegerField(db_column='M_UnPackingID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    bomid = models.IntegerField(db_column='BomID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_UnPackingDtl'


class MUnpackingwl(models.Model):
    m_unpackingwlid = models.AutoField(db_column='M_UnPackingWLID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    m_unpackingid = models.IntegerField(db_column='M_UnPackingID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bomid = models.IntegerField(db_column='BomID', blank=True, null=True)  # Field name made lowercase.
    m_unpackingdtlid = models.IntegerField(db_column='M_UnPackingDtlID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_UnPackingWL'


class Module(models.Model):
    moduleid = models.IntegerField(db_column='ModuleID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Module'


class Months(models.Model):
    monthsid = models.IntegerField(db_column='MonthsID', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Months'
        unique_together = (('monthsid', 'caption'),)


class Movemoney(models.Model):
    movemoneyid = models.IntegerField(db_column='MoveMoneyID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    bankoutid = models.IntegerField(db_column='BankOutID', blank=True, null=True)  # Field name made lowercase.
    bankinid = models.IntegerField(db_column='BankInID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MoveMoney'


class Onhand(models.Model):
    onhandid = models.AutoField(db_column='OnhandID', primary_key=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID')  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty')  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Onhand'


class Operator(models.Model):
    operatorid = models.AutoField(db_column='OperatorID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    isoperator = models.IntegerField(db_column='isOperator', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='pass', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    descript = models.CharField(max_length=100, blank=True, null=True)
    mustchangepass = models.IntegerField(blank=True, null=True)
    canchangepass = models.IntegerField(blank=True, null=True)
    sysmanager = models.IntegerField(db_column='SysManager', blank=True, null=True)  # Field name made lowercase.
    viewotherdata = models.IntegerField(db_column='ViewOtherData', blank=True, null=True)  # Field name made lowercase.
    editotherdata = models.IntegerField(db_column='EditOtherData', blank=True, null=True)  # Field name made lowercase.
    checkselfbill = models.IntegerField(db_column='CheckSelfBill', blank=True, null=True)  # Field name made lowercase.
    hidecheckedbill = models.IntegerField(db_column='HideCheckedBill', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Operator'


class Operatordept(models.Model):
    operatorid = models.IntegerField(db_column='OperatorID', primary_key=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID')  # Field name made lowercase.
    edit = models.IntegerField(db_column='Edit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperatorDept'
        unique_together = (('operatorid', 'deptid'),)


class Operatoremp(models.Model):
    operatorid = models.IntegerField(db_column='OperatorID', primary_key=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID')  # Field name made lowercase.
    edit = models.IntegerField(db_column='Edit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperatorEmp'
        unique_together = (('operatorid', 'empid'),)


class Operatorgroup(models.Model):
    operatorid = models.IntegerField(db_column='OperatorID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperatorGroup'
        unique_together = (('operatorid', 'groupid'),)


class Operatorshop(models.Model):
    operatorid = models.IntegerField(db_column='OperatorID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID')  # Field name made lowercase.
    edit = models.IntegerField(db_column='Edit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperatorShop'
        unique_together = (('operatorid', 'shopid'),)


class Otherin(models.Model):
    otherinid = models.IntegerField(db_column='OtherInID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OtherIn'


class Otherindtl(models.Model):
    otherindtlid = models.AutoField(db_column='OtherInDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    otherinid = models.IntegerField(db_column='OtherInID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OtherInDtl'


class Otherout(models.Model):
    otheroutid = models.IntegerField(db_column='OtherOutID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OtherOut'


class Otheroutdtl(models.Model):
    otheroutdtlid = models.AutoField(db_column='OtherOutDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    otheroutid = models.IntegerField(db_column='OtherOutID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OtherOutDtl'


class Overtime(models.Model):
    overtimeid = models.IntegerField(db_column='OverTimeID', primary_key=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OverTime'


class Pay(models.Model):
    payid = models.IntegerField(db_column='PayID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    factamt = models.FloatField(db_column='FactAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay'


class Paydtl(models.Model):
    paydtlid = models.AutoField(db_column='PayDtlID', primary_key=True)  # Field name made lowercase.
    payid = models.IntegerField(db_column='PayID')  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PayDtl'


class Piecework(models.Model):
    pieceworkid = models.IntegerField(db_column='PieceWorkID', primary_key=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    workproid = models.IntegerField(db_column='WorkProID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PieceWork'


class Plusminus(models.Model):
    plusminusid = models.IntegerField(db_column='PlusMinusID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlusMinus'


class Priceadjustment(models.Model):
    priceadjustmentid = models.IntegerField(db_column='PriceAdjustmentID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceAdjustment'


class Priceadjustmentdtl(models.Model):
    priceadjustmentdtlid = models.AutoField(db_column='PriceAdjustmentDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    priceadjustmentid = models.IntegerField(db_column='PriceAdjustmentID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    storeqty = models.FloatField(db_column='StoreQty', blank=True, null=True)  # Field name made lowercase.
    oldprice = models.FloatField(db_column='OldPrice', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceAdjustmentDtl'


class Priceinfo(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spec = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    p1 = models.FloatField(blank=True, null=True)
    p2 = models.FloatField(blank=True, null=True)
    p3 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PriceInfo'


class Printset(models.Model):
    printsetid = models.AutoField(db_column='PrintSetID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    topmargin = models.FloatField(db_column='TopMargin', blank=True, null=True)  # Field name made lowercase.
    bottommargin = models.FloatField(db_column='BottomMargin', blank=True, null=True)  # Field name made lowercase.
    leftmargin = models.FloatField(db_column='LeftMargin', blank=True, null=True)  # Field name made lowercase.
    rightmargin = models.FloatField(db_column='RightMargin', blank=True, null=True)  # Field name made lowercase.
    fitwidthtopage = models.IntegerField(db_column='FitWidthToPage', blank=True, null=True)  # Field name made lowercase.
    printfontname = models.CharField(db_column='PrintFontName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    autostretch = models.IntegerField(db_column='AutoStretch', blank=True, null=True)  # Field name made lowercase.
    colored = models.IntegerField(db_column='Colored', blank=True, null=True)  # Field name made lowercase.
    fitingbycolwidths = models.IntegerField(db_column='FitingByColWidths', blank=True, null=True)  # Field name made lowercase.
    optimalcolwidths = models.IntegerField(db_column='OptimalColWidths', blank=True, null=True)  # Field name made lowercase.
    islandscape = models.IntegerField(db_column='IsLandScape', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrintSet'



class Printtemplate(models.Model):
    printtemplateid = models.AutoField(db_column='PrintTemplateID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    grid = models.IntegerField(db_column='Grid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrintTemplate'


class Purchase(models.Model):
    purchaseid = models.IntegerField(db_column='PurchaseID', primary_key=True)  # Field name made lowercase.
    shopid = models.ForeignKey(to='Shop',db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdisc = models.FloatField(db_column='BillDisc', blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    cashamt = models.FloatField(db_column='CashAmt', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PaidAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Purchase'


class Purchaseassess(models.Model):
    purchaseassessid = models.IntegerField(db_column='PurchaseAssessID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    purchasefinished = models.IntegerField(db_column='PurchaseFinished', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseAssess'


class Purchaseassessdtl(models.Model):
    purchaseassessdtlid = models.AutoField(db_column='PurchaseAssessDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    purchaseassessid = models.IntegerField(db_column='PurchaseAssessID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    purchaseqty = models.FloatField(db_column='PurchaseQty', blank=True, null=True)  # Field name made lowercase.
    purchaseamt = models.FloatField(db_column='PurchaseAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseAssessDtl'


class Purchasedtl(models.Model):
    purchasedtlid = models.AutoField(db_column='PurchaseDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    purchaseid = models.IntegerField(db_column='PurchaseID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    discprice = models.FloatField(db_column='DiscPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.FloatField(db_column='TaxRate', blank=True, null=True)  # Field name made lowercase.
    taxamt = models.FloatField(db_column='TaxAmt', blank=True, null=True)  # Field name made lowercase.
    totalamt = models.FloatField(db_column='TotalAmt', blank=True, null=True)  # Field name made lowercase.
    isgift = models.IntegerField(db_column='IsGift', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    purchaseinqty = models.FloatField(db_column='PurchaseInQty', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseDtl'


class Purchasein(models.Model):
    purchaseinid = models.IntegerField(db_column='PurchaseInID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    factamt = models.FloatField(db_column='FactAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PaidAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseIn'


class Purchaseindtl(models.Model):
    purchaseindtlid = models.AutoField(db_column='PurchaseInDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    purchaseinid = models.IntegerField(db_column='PurchaseInID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    purchasertnqty = models.FloatField(db_column='PurchaseRtnQty', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseInDtl'


class Purchaseorder(models.Model):
    purchaseorderid = models.IntegerField(db_column='PurchaseOrderID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    billdisc = models.FloatField(db_column='BillDisc', blank=True, null=True)  # Field name made lowercase.
    terminate = models.IntegerField(db_column='Terminate', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    purchaseassessfinished = models.IntegerField(db_column='PurchaseAssessFinished', blank=True, null=True)  # Field name made lowercase.
    purchasefinished = models.IntegerField(db_column='PurchaseFinished', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseOrder'


class Purchaseorderdtl(models.Model):
    purchaseorderdtlid = models.AutoField(db_column='PurchaseOrderDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    purchaseorderid = models.IntegerField(db_column='PurchaseOrderID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    discprice = models.FloatField(db_column='DiscPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.FloatField(db_column='TaxRate', blank=True, null=True)  # Field name made lowercase.
    taxamt = models.FloatField(db_column='TaxAmt', blank=True, null=True)  # Field name made lowercase.
    totalamt = models.FloatField(db_column='TotalAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    purchaseassessqty = models.FloatField(db_column='PurchaseAssessQty', blank=True, null=True)  # Field name made lowercase.
    purchaseqty = models.FloatField(db_column='PurchaseQty', blank=True, null=True)  # Field name made lowercase.
    dterminate = models.IntegerField(db_column='DTerminate', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseOrderDtl'


class Purchaseplan(models.Model):
    purchaseplanid = models.IntegerField(db_column='PurchasePlanID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    terminate = models.IntegerField(db_column='Terminate', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchasePlan'


class Purchaseplandtl(models.Model):
    purchaseplandtlid = models.AutoField(db_column='PurchasePlanDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    purchaseplanid = models.IntegerField(db_column='PurchasePlanID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    purchaseorderqty = models.FloatField(db_column='PurchaseOrderQty', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchasePlanDtl'


class Purchaseprice(models.Model):
    purchasepriceid = models.IntegerField(db_column='PurchasePriceID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchasePrice'


class Purchasepricedtl(models.Model):
    purchasepricedtlid = models.AutoField(db_column='PurchasePriceDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    purchasepriceid = models.IntegerField(db_column='PurchasePriceID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchasePriceDtl'


class Purchasertn(models.Model):
    purchasertnid = models.IntegerField(db_column='PurchaseRtnID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bianhao = models.CharField(db_column='BianHao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chukuid = models.CharField(db_column='ChuKuID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chukudanhao = models.CharField(db_column='ChuKuDanHao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dingdanid = models.CharField(db_column='DingDanID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseRtn'


class Purchasertndtl(models.Model):
    purchasertndtlid = models.AutoField(db_column='PurchaseRtnDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    purchasertnid = models.IntegerField(db_column='PurchaseRtnID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tuihuoyuanyin = models.CharField(db_column='TuiHuoYuanYin', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseRtnDtl'


class Report(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    sn = models.IntegerField(db_column='Sn', blank=True, null=True)  # Field name made lowercase.
    datefilter = models.IntegerField(db_column='DateFilter', blank=True, null=True)  # Field name made lowercase.
    titlebutton = models.IntegerField(db_column='TitleButton', blank=True, null=True)  # Field name made lowercase.
    autosum = models.IntegerField(db_column='AutoSum', blank=True, null=True)  # Field name made lowercase.
    autocolwidth = models.IntegerField(db_column='AutoColWidth', blank=True, null=True)  # Field name made lowercase.
    showgroup = models.IntegerField(db_column='ShowGroup', blank=True, null=True)  # Field name made lowercase.
    showtitlefilter = models.IntegerField(db_column='ShowTitleFilter', blank=True, null=True)  # Field name made lowercase.
    footerrowcount = models.IntegerField(db_column='FooterRowCount', blank=True, null=True)  # Field name made lowercase.
    reportprocid = models.IntegerField(db_column='ReportProcID', blank=True, null=True)  # Field name made lowercase.
    operatorfilter = models.IntegerField(db_column='OperatorFilter', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    procname = models.CharField(db_column='ProcName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pcolumn = models.CharField(db_column='PColumn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preportfilteritemid = models.IntegerField(db_column='PReportFilterItemID', blank=True, null=True)  # Field name made lowercase.
    pfilteroperatedtlid = models.IntegerField(db_column='PFilterOperateDtlID', blank=True, null=True)  # Field name made lowercase.
    billtype = models.IntegerField(db_column='BillType', blank=True, null=True)  # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType', blank=True, null=True)  # Field name made lowercase.
    reportrowid = models.IntegerField(db_column='ReportRowID', blank=True, null=True)  # Field name made lowercase.
    reportcolid = models.IntegerField(db_column='ReportColID', blank=True, null=True)  # Field name made lowercase.
    reportcolasparam = models.IntegerField(db_column='ReportColAsParam', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    datafilter = models.CharField(db_column='DataFilter', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    filtertext = models.CharField(db_column='FilterText', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Report'


class Reportbilltype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportBillType'


class Reportcallparam(models.Model):
    reportid = models.IntegerField(db_column='ReportID', primary_key=True)  # Field name made lowercase.
    sn = models.IntegerField(db_column='Sn')  # Field name made lowercase.
    titlecaption = models.CharField(db_column='TitleCaption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    filteritemid = models.IntegerField(db_column='FilterItemID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportCallParam'
        unique_together = (('reportid', 'sn'),)


class Reportcol(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datafield = models.CharField(db_column='DataField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titledataset = models.TextField(db_column='TitleDataSet', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportCol'


class Reportcolumnset(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reportid = models.IntegerField(db_column='ReportID', blank=True, null=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    titlecaption = models.CharField(db_column='TitleCaption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titlebutton = models.IntegerField(db_column='TitleButton', blank=True, null=True)  # Field name made lowercase.
    footervaluetype = models.IntegerField(db_column='FooterValueType', blank=True, null=True)  # Field name made lowercase.
    footervalue = models.CharField(db_column='FooterValue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iscurrency = models.IntegerField(db_column='isCurrency', blank=True, null=True)  # Field name made lowercase.
    israte = models.IntegerField(db_column='IsRate', blank=True, null=True)  # Field name made lowercase.
    showthousands = models.IntegerField(db_column='ShowThousands', blank=True, null=True)  # Field name made lowercase.
    hideduplicates = models.IntegerField(db_column='HideDuplicates', blank=True, null=True)  # Field name made lowercase.
    tablefieldid = models.IntegerField(db_column='TableFieldID', blank=True, null=True)  # Field name made lowercase.
    footertype = models.IntegerField(db_column='FooterType', blank=True, null=True)  # Field name made lowercase.
    rpttype = models.IntegerField(db_column='RptType', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportColumnSet'


class Reportdatafilter(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reportid = models.IntegerField(db_column='ReportID')  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    reportfilteritemid = models.IntegerField(db_column='ReportFilterItemID', blank=True, null=True)  # Field name made lowercase.
    filteroperatedtlid = models.IntegerField(db_column='FilterOperateDtlID', blank=True, null=True)  # Field name made lowercase.
    filtervalue = models.CharField(db_column='FilterValue', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportDataFilter'


class Reportdatatype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datafield = models.CharField(db_column='DataField', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportDataType'


class Reportfilter(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reportid = models.IntegerField(db_column='ReportID')  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    reportfilteritemid = models.IntegerField(db_column='ReportFilterItemID', blank=True, null=True)  # Field name made lowercase.
    filteroperatedtlid = models.IntegerField(db_column='FilterOperateDtlID', blank=True, null=True)  # Field name made lowercase.
    filtervalue = models.CharField(db_column='FilterValue', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportFilter'


class Reportfilteritem(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sn = models.IntegerField(db_column='Sn', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datafield = models.CharField(db_column='DataField', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType', blank=True, null=True)  # Field name made lowercase.
    filteroperateid = models.IntegerField(db_column='FilterOperateID', blank=True, null=True)  # Field name made lowercase.
    ctrltype = models.IntegerField(db_column='CtrlType', blank=True, null=True)  # Field name made lowercase.
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportFilterItem'


class Reportparam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctrltype = models.IntegerField(db_column='CtrlType', blank=True, null=True)  # Field name made lowercase.
    ctrlvisible = models.IntegerField(db_column='CtrlVisible', blank=True, null=True)  # Field name made lowercase.
    ctrlwidth = models.IntegerField(db_column='CtrlWidth', blank=True, null=True)  # Field name made lowercase.
    radiogroupitems = models.CharField(db_column='RadioGroupItems', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datasetsql = models.CharField(db_column='DataSetSql', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tag = models.IntegerField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    readonly = models.IntegerField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportParam'


class Reportproc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    procname = models.CharField(db_column='ProcName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportProc'


class Reportprocparam(models.Model):
    reportprocid = models.IntegerField(db_column='ReportProcID', primary_key=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial')  # Field name made lowercase.
    reportparamid = models.IntegerField(db_column='ReportParamID')  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportProcParam'
        unique_together = (('reportprocid', 'serial'),)


class Reportpubparam(models.Model):
    windowid = models.IntegerField(db_column='WindowID', primary_key=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    reportparamid = models.IntegerField(db_column='ReportParamID')  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportPubParam'
        unique_together = (('windowid', 'reportparamid'),)


class Reportrow(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datafield = models.CharField(db_column='DataField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titledataset = models.TextField(db_column='TitleDataSet', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportRow'


class Reportset(models.Model):
    reportid = models.IntegerField(db_column='ReportID', primary_key=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID')  # Field name made lowercase.
    autocolwidth = models.IntegerField(db_column='AutoColWidth', blank=True, null=True)  # Field name made lowercase.
    columnset = models.TextField(db_column='ColumnSet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportSet'
        unique_together = (('reportid', 'operatorid'),)


class Requisition(models.Model):
    requisitionid = models.IntegerField(db_column='RequisitionID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    storeoutid = models.IntegerField(db_column='StoreOutID', blank=True, null=True)  # Field name made lowercase.
    storeinid = models.IntegerField(db_column='StoreInID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Requisition'


class Requisitiondtl(models.Model):
    requisitiondtlid = models.AutoField(db_column='RequisitionDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    requisitionid = models.IntegerField(db_column='RequisitionID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RequisitionDtl'


class Rights(models.Model):
    rightsid = models.AutoField(db_column='RightsID', primary_key=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    rbrowse = models.IntegerField(db_column='RBrowse', blank=True, null=True)  # Field name made lowercase.
    radd = models.IntegerField(db_column='RAdd', blank=True, null=True)  # Field name made lowercase.
    redit = models.IntegerField(db_column='REdit', blank=True, null=True)  # Field name made lowercase.
    rdel = models.IntegerField(db_column='RDel', blank=True, null=True)  # Field name made lowercase.
    rexe = models.IntegerField(db_column='RExe', blank=True, null=True)  # Field name made lowercase.
    rcheck = models.IntegerField(db_column='RCheck', blank=True, null=True)  # Field name made lowercase.
    runcheck = models.IntegerField(db_column='RUnCheck', blank=True, null=True)  # Field name made lowercase.
    rrecheck = models.IntegerField(db_column='RRecheck', blank=True, null=True)  # Field name made lowercase.
    rinvalid = models.IntegerField(db_column='RInvalid', blank=True, null=True)  # Field name made lowercase.
    rprint = models.IntegerField(db_column='RPrint', blank=True, null=True)  # Field name made lowercase.
    rprintset = models.IntegerField(db_column='RPrintSet', blank=True, null=True)  # Field name made lowercase.
    filterstr = models.CharField(db_column='FilterStr', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    filtertext = models.CharField(db_column='FilterText', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rights'


class Rptcall(models.Model):
    rptcallid = models.AutoField(db_column='RptCallID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    calltype = models.IntegerField(db_column='CallType', blank=True, null=True)  # Field name made lowercase.
    callwindowid = models.IntegerField(db_column='CallWindowID', blank=True, null=True)  # Field name made lowercase.
    param1 = models.CharField(db_column='Param1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    param2 = models.CharField(db_column='Param2', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptCall'


class Rptcalldtl(models.Model):
    rptcalldtlid = models.AutoField(db_column='RptCallDtlID', primary_key=True)  # Field name made lowercase.
    rptcallid = models.IntegerField(db_column='RptCallID', blank=True, null=True)  # Field name made lowercase.
    rptparamserial = models.IntegerField(db_column='RptParamSerial', blank=True, null=True)  # Field name made lowercase.
    rowparam = models.CharField(db_column='RowParam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rowcaption = models.CharField(db_column='RowCaption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rowtable = models.CharField(db_column='RowTable', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rowfield = models.CharField(db_column='RowField', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colparam = models.CharField(db_column='ColParam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colcaptions = models.CharField(db_column='ColCaptions', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colvalues = models.CharField(db_column='ColValues', max_length=50, blank=True, null=True)  # Field name made lowercase.
    titlecaption = models.CharField(db_column='TitleCaption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filteritemid = models.IntegerField(db_column='FilterItemID', blank=True, null=True)  # Field name made lowercase.
    filteroperatedtlid = models.IntegerField(db_column='FilterOperateDtlID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptCallDtl'


class Rptcallparam(models.Model):
    rptcallparamid = models.AutoField(db_column='RptCallParamID', primary_key=True)  # Field name made lowercase.
    rptcallid = models.IntegerField(db_column='RptCallID', blank=True, null=True)  # Field name made lowercase.
    rptparamserial = models.IntegerField(db_column='RptParamSerial', blank=True, null=True)  # Field name made lowercase.
    rptparamid = models.IntegerField(db_column='RptParamID', blank=True, null=True)  # Field name made lowercase.
    callrptparamid = models.IntegerField(db_column='CallRptParamID', blank=True, null=True)  # Field name made lowercase.
    valuetype = models.IntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    passvalue = models.CharField(db_column='PassValue', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptCallParam'


class Rptcol(models.Model):
    rptcolid = models.IntegerField(db_column='RptColID', primary_key=True)  # Field name made lowercase.
    datafield = models.CharField(db_column='DataField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titledataset = models.TextField(db_column='TitleDataSet', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reportfilteritemid = models.IntegerField(db_column='ReportFilterItemID', blank=True, null=True)  # Field name made lowercase.
    filteroperatedtlid = models.IntegerField(db_column='FilterOperateDtlID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptCol'


class Rptmonth(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptMonth'


class Rptparam(models.Model):
    rptparamid = models.AutoField(db_column='RptParamID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctrltype = models.IntegerField(db_column='CtrlType', blank=True, null=True)  # Field name made lowercase.
    ctrlvisible = models.IntegerField(db_column='CtrlVisible', blank=True, null=True)  # Field name made lowercase.
    ctrlwidth = models.IntegerField(db_column='CtrlWidth', blank=True, null=True)  # Field name made lowercase.
    radiogroupitems = models.CharField(db_column='RadioGroupItems', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datasetsql = models.CharField(db_column='DataSetSql', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tag = models.IntegerField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    readonly = models.IntegerField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.
    rptsubtype = models.IntegerField(db_column='RptSubType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptParam'


class Rptrow(models.Model):
    rptrowid = models.IntegerField(db_column='RptRowID', primary_key=True)  # Field name made lowercase.
    datafield = models.CharField(db_column='DataField', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titledataset = models.TextField(db_column='TitleDataSet', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptRow'


class Rptset(models.Model):
    rptsetid = models.IntegerField(db_column='RptSetID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    rptsubtypeserial = models.IntegerField(db_column='RptSubTypeSerial', blank=True, null=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titlebutton = models.IntegerField(db_column='TitleButton', blank=True, null=True)  # Field name made lowercase.
    footervaluetype = models.IntegerField(db_column='FooterValueType', blank=True, null=True)  # Field name made lowercase.
    footervalue = models.CharField(db_column='FooterValue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iscurrency = models.IntegerField(db_column='isCurrency', blank=True, null=True)  # Field name made lowercase.
    israte = models.IntegerField(db_column='IsRate', blank=True, null=True)  # Field name made lowercase.
    showthousands = models.IntegerField(db_column='ShowThousands', blank=True, null=True)  # Field name made lowercase.
    hideduplicates = models.IntegerField(db_column='HideDuplicates', blank=True, null=True)  # Field name made lowercase.
    tablefieldid = models.IntegerField(db_column='TableFieldID', blank=True, null=True)  # Field name made lowercase.
    footertype = models.IntegerField(db_column='FooterType', blank=True, null=True)  # Field name made lowercase.
    rpttype = models.IntegerField(db_column='RptType', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptSet'


class Rptsets(models.Model):
    rptsetsid = models.AutoField(db_column='RptSetsID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    billwindowid = models.IntegerField(db_column='BillWindowID', blank=True, null=True)  # Field name made lowercase.
    rpttype = models.IntegerField(db_column='RptType', blank=True, null=True)  # Field name made lowercase.
    columnset = models.CharField(db_column='ColumnSet', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    datefilter = models.IntegerField(db_column='DateFilter', blank=True, null=True)  # Field name made lowercase.
    operatorfilter = models.IntegerField(db_column='OperatorFilter', blank=True, null=True)  # Field name made lowercase.
    titlebutton = models.IntegerField(db_column='TitleButton', blank=True, null=True)  # Field name made lowercase.
    autosum = models.IntegerField(db_column='AutoSum', blank=True, null=True)  # Field name made lowercase.
    showgroup = models.IntegerField(db_column='ShowGroup', blank=True, null=True)  # Field name made lowercase.
    showfilter = models.IntegerField(db_column='ShowFilter', blank=True, null=True)  # Field name made lowercase.
    footerrowcount = models.IntegerField(db_column='FooterRowCount', blank=True, null=True)  # Field name made lowercase.
    autocolwidth = models.IntegerField(db_column='AutoColWidth', blank=True, null=True)  # Field name made lowercase.
    charttype = models.IntegerField(db_column='ChartType', blank=True, null=True)  # Field name made lowercase.
    loginshow = models.IntegerField(db_column='LoginShow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptSets'


class Rptsubtype(models.Model):
    rptsubtypeid = models.IntegerField(db_column='RptSubTypeID')  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', primary_key=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    columnset = models.CharField(db_column='ColumnSet', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    paramvalue = models.IntegerField(db_column='ParamValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptSubType'
        unique_together = (('windowid', 'serial'),)


class Rptsumtype(models.Model):
    rptsumtypeid = models.AutoField(db_column='RptSumTypeID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RptSumType'


class Salary(models.Model):
    salaryid = models.IntegerField(db_column='SalaryID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=50)  # Field name made lowercase.
    wageyear = models.IntegerField(db_column='WageYear', blank=True, null=True)  # Field name made lowercase.
    wagemonth = models.IntegerField(db_column='WageMonth', blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    factamt = models.FloatField(db_column='FactAmt', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salary'


class Sale(models.Model):
    saleid = models.IntegerField(db_column='SaleID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='ReCheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.ForeignKey(db_column='ClientID',to='Client')  # Field name made lowercase.
    bankid = models.IntegerField(db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    daysofpayment = models.IntegerField(db_column='DaysOfPayment', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='ReCheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billdisc = models.FloatField(db_column='BillDisc', blank=True, null=True)  # Field name made lowercase.
    cashamt = models.FloatField(db_column='CashAmt', blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PaidAmt', blank=True, null=True)  # Field name made lowercase.
    rtnamt = models.FloatField(db_column='RtnAmt', blank=True, null=True)  # Field name made lowercase.
    factamt = models.FloatField(db_column='FactAmt', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    billnumber = models.CharField(db_column='BillNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    saleoutfinished = models.IntegerField(db_column='SaleOutFinished', blank=True, null=True)  # Field name made lowercase.
    isnewclient = models.IntegerField(db_column='IsNewClient', blank=True, null=True)  # Field name made lowercase.
    peihuo1 = models.IntegerField(db_column='PeiHuo1', blank=True, null=True)  # Field name made lowercase.
    peihuo2 = models.IntegerField(db_column='PeiHuo2', blank=True, null=True)  # Field name made lowercase.
    duihuo = models.IntegerField(db_column='DuiHuo', blank=True, null=True)  # Field name made lowercase.
    siji = models.IntegerField(db_column='SiJi', blank=True, null=True)  # Field name made lowercase.
    genche = models.IntegerField(db_column='GenChe', blank=True, null=True)  # Field name made lowercase.
    zhuangche = models.IntegerField(db_column='ZhuangChe', blank=True, null=True)  # Field name made lowercase.
    shoukuan = models.IntegerField(db_column='ShouKuan', blank=True, null=True)  # Field name made lowercase.
    sancang = models.IntegerField(db_column='SanCang', blank=True, null=True)  # Field name made lowercase.
    huidanhao = models.CharField(db_column='HuiDanHao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dingdanhao = models.CharField(db_column='DingDanHao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    weborder = models.CharField(db_column='WebOrder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billcharged = models.IntegerField(db_column='BillCharged', blank=True, null=True)  # Field name made lowercase.
    billunpaid = models.IntegerField(db_column='BillUnPaid', blank=True, null=True)  # Field name made lowercase.
    monthpay = models.IntegerField(db_column='MonthPay', blank=True, null=True)  # Field name made lowercase.
    unprinted = models.IntegerField(db_column='UnPrinted', blank=True, null=True)  # Field name made lowercase.
    chargeempid = models.IntegerField(db_column='ChargeEmpID', blank=True, null=True)  # Field name made lowercase.
    chargememo = models.CharField(db_column='ChargeMemo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    huodaofukuan = models.IntegerField(db_column='HuoDaoFuKuan', blank=True, null=True)  # Field name made lowercase.
    isout = models.IntegerField(db_column='IsOut', blank=True, null=True)  # Field name made lowercase.
    outdate = models.DateTimeField(db_column='OutDate', blank=True, null=True)  # Field name made lowercase.
    outmemo = models.CharField(db_column='OutMemo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-saleid']
        managed = False
        db_table = 'Sale'

    def __str__(self):
        return str(self.saleid)


class Saledtl(models.Model):
    saledtlid = models.AutoField(db_column='SaleDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    saleid = models.ForeignKey(to='Sale',db_column='SaleID')  # Field name made lowercase.
    goodsid = models.ForeignKey(to='Goods',db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    aprice = models.FloatField(db_column='APrice', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    discprice = models.FloatField(db_column='DiscPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.FloatField(db_column='TaxRate', blank=True, null=True)  # Field name made lowercase.
    taxamt = models.FloatField(db_column='TaxAmt', blank=True, null=True)  # Field name made lowercase.
    totalamt = models.FloatField(db_column='TotalAmt', blank=True, null=True)  # Field name made lowercase.
    isgift = models.IntegerField(db_column='IsGift', blank=True, null=True)  # Field name made lowercase.
    isnewgoods = models.IntegerField(db_column='IsNewGoods', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    dstoreid = models.IntegerField(db_column='DStoreID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mark = models.CharField(db_column='Mark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    saleoutqty = models.FloatField(db_column='SaleOutQty', blank=True, null=True)  # Field name made lowercase.
    salertnqty = models.FloatField(db_column='SaleRtnQty', blank=True, null=True)  # Field name made lowercase.
    salertngoodsamt = models.FloatField(db_column='SaleRtnGoodsAmt', blank=True, null=True)  # Field name made lowercase.
    tuihuoyuanyin = models.CharField(db_column='TuiHuoYuanYin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    huowei = models.CharField(db_column='HuoWei', max_length=50, blank=True, null=True)  # Field name made lowercase.
    calculated = models.IntegerField(db_column='Calculated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleDtl'


class Saleorder(models.Model):
    saleorderid = models.IntegerField(db_column='SaleOrderID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    billdisc = models.FloatField(db_column='BillDisc', blank=True, null=True)  # Field name made lowercase.
    terminate = models.IntegerField(db_column='Terminate', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    finished = models.IntegerField(db_column='Finished', blank=True, null=True)  # Field name made lowercase.
    modeofpayment = models.CharField(db_column='ModeOfPayment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    salefinished = models.IntegerField(db_column='SaleFinished', blank=True, null=True)  # Field name made lowercase.
    saleoutfinished = models.IntegerField(db_column='SaleOutFinished', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleOrder'


class Saleorderdtl(models.Model):
    saleorderdtlid = models.AutoField(db_column='SaleOrderDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    saleorderid = models.IntegerField(db_column='SaleOrderID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    discprice = models.FloatField(db_column='DiscPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.FloatField(db_column='TaxRate', blank=True, null=True)  # Field name made lowercase.
    taxamt = models.FloatField(db_column='TaxAmt', blank=True, null=True)  # Field name made lowercase.
    totalamt = models.FloatField(db_column='TotalAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    saleqty = models.FloatField(db_column='SaleQty', blank=True, null=True)  # Field name made lowercase.
    saleoutqty = models.FloatField(db_column='SaleOutQty', blank=True, null=True)  # Field name made lowercase.
    dterminate = models.IntegerField(db_column='DTerminate', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isgift = models.IntegerField(db_column='IsGift', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleOrderDtl'


class Saleout(models.Model):
    saleoutid = models.IntegerField(db_column='SaleOutID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='ReCheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='ReCheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='Linkman', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='Shipto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleOut'


class Saleoutdtl(models.Model):
    saleoutdtlid = models.AutoField(db_column='SaleOutDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    saleoutid = models.IntegerField(db_column='SaleOutID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    salertnqty = models.FloatField(db_column='SaleRtnQty', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleOutDtl'


class Saleplan(models.Model):
    saleplanid = models.IntegerField(db_column='SalePlanID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    terminate = models.IntegerField(db_column='Terminate', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalePlan'


class Saleplandtl(models.Model):
    saleplandtlid = models.AutoField(db_column='SalePlanDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    saleplanid = models.IntegerField(db_column='SalePlanID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    saleorderqty = models.FloatField(db_column='SaleOrderQty', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalePlanDtl'


class Saleprepare(models.Model):
    saleprepareid = models.IntegerField(db_column='SalePrepareID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='ShipTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalePrepare'


class Salepreparedtl(models.Model):
    salepreparedtlid = models.AutoField(db_column='SalePrepareDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    saleprepareid = models.IntegerField(db_column='SalePrepareID')  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    saleoutqty = models.FloatField(db_column='SaleOutQty', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalePrepareDtl'


class Saleprice(models.Model):
    salepriceid = models.IntegerField(db_column='SalePriceID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalePrice'


class Salepriceclienttype(models.Model):
    salepriceclienttypeid = models.AutoField(db_column='SalePriceClientTypeID', primary_key=True)  # Field name made lowercase.
    salepriceid = models.IntegerField(db_column='SalePriceID', blank=True, null=True)  # Field name made lowercase.
    clienttypeid = models.IntegerField(db_column='ClientTypeID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalePriceClientType'


class Salepricedtl(models.Model):
    salepricedtlid = models.AutoField(db_column='SalePriceDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    salepriceid = models.IntegerField(db_column='SalePriceID')  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalePriceDtl'


class Salertn(models.Model):
    salertnid = models.IntegerField(db_column='SaleRtnID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='RecheckID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    salesmanid = models.IntegerField(db_column='SalesManID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='RecheckDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billamt = models.FloatField(db_column='BillAmt', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipto = models.CharField(db_column='Shipto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    huidan = models.CharField(db_column='HuiDan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    siji = models.IntegerField(db_column='SiJi', blank=True, null=True)  # Field name made lowercase.
    weborder = models.CharField(db_column='WebOrder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuihuoren = models.CharField(db_column='TuiHuoRen', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yanshouren = models.CharField(db_column='YanShouRen', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleRtn'


class Salertndtl(models.Model):
    salertndtlid = models.AutoField(db_column='SaleRtnDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    salertnid = models.IntegerField(db_column='SaleRtnID')  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    goodsunitid = models.IntegerField(db_column='GoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    aprice = models.FloatField(blank=True, null=True)
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    pcsqty = models.CharField(db_column='PcsQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assistqty = models.FloatField(db_column='AssistQty', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    unitqty = models.FloatField(db_column='UnitQty', blank=True, null=True)  # Field name made lowercase.
    goodsamt = models.FloatField(db_column='GoodsAmt', blank=True, null=True)  # Field name made lowercase.
    referwindowid = models.IntegerField(db_column='ReferWindowID', blank=True, null=True)  # Field name made lowercase.
    referbillid = models.IntegerField(db_column='ReferBillID', blank=True, null=True)  # Field name made lowercase.
    referdtlid = models.IntegerField(db_column='ReferDtlID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo1 = models.CharField(db_column='Memo1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo2 = models.CharField(db_column='Memo2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo3 = models.CharField(db_column='Memo3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo4 = models.CharField(db_column='Memo4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo5 = models.CharField(db_column='Memo5', max_length=200, blank=True, null=True)  # Field name made lowercase.
    jushou = models.IntegerField(db_column='JuShou', blank=True, null=True)  # Field name made lowercase.
    maiyisongyi = models.IntegerField(db_column='MaiYiSongYi', blank=True, null=True)  # Field name made lowercase.
    tuihuoyuanyin = models.CharField(db_column='TuiHuoYuanYin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mark = models.CharField(db_column='Mark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isgift = models.IntegerField(db_column='IsGift', blank=True, null=True)  # Field name made lowercase.
    calculated = models.IntegerField(db_column='Calculated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleRtnDtl'


class Sex(models.Model):
    sexid = models.IntegerField(db_column='SexID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sex'



class Shop(models.Model):
    shopid = models.IntegerField(db_column='ShopID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    legalrep = models.CharField(db_column='LegalRep', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxno = models.CharField(db_column='Taxno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shop'

    def __str__(self):
        return self.name


class Store(models.Model):
    storeid = models.IntegerField(db_column='StoreID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    iswaste = models.IntegerField(db_column='IsWaste', blank=True, null=True)  # Field name made lowercase.
    isweb = models.IntegerField(db_column='IsWeb', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Store'


class Subreport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID')  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    procname = models.CharField(db_column='ProcName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    rpttype = models.IntegerField(db_column='RptType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubReport'


class Tsum(models.Model):
    tsumid = models.IntegerField(db_column='TSumID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    recheckid = models.IntegerField(db_column='ReCheckID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    invalidid = models.IntegerField(db_column='InvalidID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    recheckdate = models.DateTimeField(db_column='ReCheckDate', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    invaliddate = models.DateTimeField(db_column='InvalidDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    invalid = models.IntegerField(db_column='Invalid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TSum'


class Tsumdtl(models.Model):
    tsumdtlid = models.AutoField(db_column='TSumDtlID', primary_key=True)  # Field name made lowercase.
    tsumid = models.IntegerField(db_column='TSumID', blank=True, null=True)  # Field name made lowercase.
    codeinput = models.CharField(db_column='CodeInput', max_length=50, blank=True, null=True)  # Field name made lowercase.
    saleid = models.IntegerField(db_column='SaleID', blank=True, null=True)  # Field name made lowercase.
    pcs = models.FloatField(db_column='Pcs', blank=True, null=True)  # Field name made lowercase.
    iscangku = models.IntegerField(db_column='IsCangKu', blank=True, null=True)  # Field name made lowercase.
    iscaiwu = models.IntegerField(db_column='IsCaiWu', blank=True, null=True)  # Field name made lowercase.
    dianhuotime = models.CharField(db_column='DianHuoTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    likaitime = models.CharField(db_column='LiKaiTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TSumDtl'


class Tablefield(models.Model):
    tablefieldid = models.AutoField(db_column='TableFieldID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID')  # Field name made lowercase.
    tabletype = models.IntegerField(db_column='TableType')  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    israte = models.IntegerField(db_column='IsRate', blank=True, null=True)  # Field name made lowercase.
    iscurrency = models.IntegerField(db_column='IsCurrency', blank=True, null=True)  # Field name made lowercase.
    rpttype = models.IntegerField(db_column='RptType', blank=True, null=True)  # Field name made lowercase.
    fieldtype = models.IntegerField(db_column='FieldType', blank=True, null=True)  # Field name made lowercase.
    formula = models.TextField(db_column='Formula', blank=True, null=True)  # Field name made lowercase.
    prec = models.IntegerField(db_column='Prec', blank=True, null=True)  # Field name made lowercase.
    ctrltype = models.IntegerField(db_column='CtrlType', blank=True, null=True)  # Field name made lowercase.
    colvisible = models.IntegerField(db_column='ColVisible', blank=True, null=True)  # Field name made lowercase.
    colfixed = models.IntegerField(db_column='ColFixed', blank=True, null=True)  # Field name made lowercase.
    colwidth = models.IntegerField(db_column='ColWidth', blank=True, null=True)  # Field name made lowercase.
    footertype = models.IntegerField(db_column='FooterType', blank=True, null=True)  # Field name made lowercase.
    hideduplicates = models.IntegerField(db_column='HideDuplicates', blank=True, null=True)  # Field name made lowercase.
    lookupfieldid = models.IntegerField(db_column='LookupFieldID', blank=True, null=True)  # Field name made lowercase.
    ctrlvisible = models.IntegerField(db_column='CtrlVisible', blank=True, null=True)  # Field name made lowercase.
    ctrlfixed = models.IntegerField(db_column='CtrlFixed', blank=True, null=True)  # Field name made lowercase.
    ctrlwidth = models.IntegerField(db_column='CtrlWidth', blank=True, null=True)  # Field name made lowercase.
    readonly = models.IntegerField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.
    tag = models.IntegerField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autocopy = models.IntegerField(db_column='AutoCopy', blank=True, null=True)  # Field name made lowercase.
    helpid = models.IntegerField(db_column='HelpID', blank=True, null=True)  # Field name made lowercase.
    refresh = models.IntegerField(db_column='Refresh', blank=True, null=True)  # Field name made lowercase.
    searchmode = models.IntegerField(db_column='SearchMode', blank=True, null=True)  # Field name made lowercase.
    autodropdown = models.IntegerField(db_column='AutoDropDown', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TableField'


class Tableformula(models.Model):
    tableformulaid = models.AutoField(db_column='TableFormulaID', primary_key=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    tabletype = models.IntegerField(db_column='TableType', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    referfields = models.CharField(db_column='ReferFields', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TableFormula'


class Tableformulareferfield(models.Model):
    tableformulaid = models.IntegerField(db_column='TableFormulaID', primary_key=True)  # Field name made lowercase.
    referfield = models.CharField(db_column='ReferField', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TableFormulaReferField'
        unique_together = (('tableformulaid', 'referfield'),)


class Target(models.Model):
    targetid = models.IntegerField(db_column='TargetID', primary_key=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    number_1 = models.FloatField(db_column='1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.FloatField(db_column='2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.FloatField(db_column='3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.FloatField(db_column='4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.FloatField(db_column='5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6 = models.FloatField(db_column='6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_7 = models.FloatField(db_column='7', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_8 = models.FloatField(db_column='8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_9 = models.FloatField(db_column='9', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_10 = models.FloatField(db_column='10', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_11 = models.FloatField(db_column='11', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_12 = models.FloatField(db_column='12', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'Target'


class Task(models.Model):
    taskid = models.IntegerField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='ShopID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    checkorid = models.IntegerField(db_column='CheckorID', blank=True, null=True)  # Field name made lowercase.
    editorid = models.IntegerField(db_column='EditorID', blank=True, null=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    printstyleid = models.IntegerField(db_column='PrintStyleID', blank=True, null=True)  # Field name made lowercase.
    printtimes = models.IntegerField(db_column='PrintTimes', blank=True, null=True)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    billcode = models.CharField(db_column='BillCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsID', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    saleorderid = models.IntegerField(db_column='SaleOrderID', blank=True, null=True)  # Field name made lowercase.
    saleorderdtlid = models.IntegerField(db_column='SaleOrderDtlID', blank=True, null=True)  # Field name made lowercase.
    trademark = models.CharField(db_column='TradeMark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bomid = models.IntegerField(db_column='BomID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task'


class Taskdtl(models.Model):
    taskdtlid = models.IntegerField(db_column='TaskDtlID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='TaskID')  # Field name made lowercase.
    subgoodsid = models.IntegerField(db_column='SubGoodsID', blank=True, null=True)  # Field name made lowercase.
    subgoodsunitid = models.IntegerField(db_column='SubGoodsUnitID', blank=True, null=True)  # Field name made lowercase.
    subqty = models.FloatField(db_column='SubQty', blank=True, null=True)  # Field name made lowercase.
    wasteqty = models.FloatField(db_column='WasteQty', blank=True, null=True)  # Field name made lowercase.
    wasterate = models.FloatField(db_column='WasteRate', blank=True, null=True)  # Field name made lowercase.
    qtyrequired = models.FloatField(db_column='QtyRequired', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskDtl'


class Taskprocess(models.Model):
    taskprocessid = models.IntegerField(db_column='TaskProcessID', primary_key=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='TaskID', blank=True, null=True)  # Field name made lowercase.
    processid = models.IntegerField(db_column='ProcessID', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskProcess'


class Truck(models.Model):
    truckid = models.IntegerField(db_column='TruckID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Truck'


class Unittype(models.Model):
    unittypeid = models.IntegerField(db_column='UnitTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnitType'


class Wagedata(models.Model):
    wagedataid = models.AutoField(db_column='WageDataID', primary_key=True)  # Field name made lowercase.
    wageyear = models.IntegerField(db_column='WageYear')  # Field name made lowercase.
    wagemonth = models.IntegerField(db_column='WageMonth')  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID')  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    userdef1 = models.FloatField(db_column='UserDef1', blank=True, null=True)  # Field name made lowercase.
    userdef2 = models.FloatField(db_column='UserDef2', blank=True, null=True)  # Field name made lowercase.
    userdef3 = models.FloatField(db_column='UserDef3', blank=True, null=True)  # Field name made lowercase.
    userdef4 = models.FloatField(db_column='UserDef4', blank=True, null=True)  # Field name made lowercase.
    userdef5 = models.FloatField(db_column='UserDef5', blank=True, null=True)  # Field name made lowercase.
    userdef6 = models.FloatField(db_column='UserDef6', blank=True, null=True)  # Field name made lowercase.
    userdef7 = models.FloatField(db_column='UserDef7', blank=True, null=True)  # Field name made lowercase.
    userdef8 = models.FloatField(db_column='UserDef8', blank=True, null=True)  # Field name made lowercase.
    userdef9 = models.FloatField(db_column='UserDef9', blank=True, null=True)  # Field name made lowercase.
    userdef10 = models.FloatField(db_column='UserDef10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WageData'


class Wageitem(models.Model):
    wageitemid = models.IntegerField(db_column='WageItemID', primary_key=True)  # Field name made lowercase.
    itemno = models.IntegerField(db_column='ItemNo', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plusminusid = models.IntegerField(db_column='PlusMinusID', blank=True, null=True)  # Field name made lowercase.
    formulaexp = models.CharField(db_column='FormulaExp', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    formulatext = models.CharField(db_column='FormulaText', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    userdefined = models.IntegerField(db_column='UserDefined', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WageItem'


class Wageitemreferfield(models.Model):
    wageitemid = models.IntegerField(db_column='WageItemID', primary_key=True)  # Field name made lowercase.
    referfield = models.CharField(db_column='ReferField', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WageItemReferField'
        unique_together = (('wageitemid', 'referfield'),)


class Webclass(models.Model):
    webclassid = models.IntegerField(db_column='WebClassID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    abtype = models.CharField(db_column='ABType', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WebClass'


class WebProducts(models.Model):
    goodsid = models.IntegerField(db_column='GoodsID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    price1 = models.FloatField(db_column='Price1', blank=True, null=True)  # Field name made lowercase.
    price2 = models.FloatField(db_column='Price2', blank=True, null=True)  # Field name made lowercase.
    price3 = models.FloatField(db_column='Price3', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Web_Products'


class Workpro(models.Model):
    workproid = models.IntegerField(db_column='WorkProID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkPro'


class Zone(models.Model):
    zoneid = models.IntegerField(db_column='ZoneID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zone'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.TextField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class MsgInfo(models.Model):
    msg_infoid = models.AutoField(db_column='msg_InfoID', primary_key=True)  # Field name made lowercase.
    senddate = models.DateTimeField(db_column='SendDate', blank=True, null=True)  # Field name made lowercase.
    sendoperatorid = models.IntegerField(db_column='SendOperatorID', blank=True, null=True)  # Field name made lowercase.
    sendoperator = models.CharField(db_column='SendOperator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    readdate = models.DateTimeField(db_column='ReadDate', blank=True, null=True)  # Field name made lowercase.
    readoperatorid = models.IntegerField(db_column='ReadOperatorID', blank=True, null=True)  # Field name made lowercase.
    readoperator = models.CharField(db_column='ReadOperator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    msg = models.CharField(db_column='Msg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    haveread = models.IntegerField(db_column='HaveRead', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'msg_Info'


class OlImage(models.Model):
    ol_imageid = models.IntegerField(db_column='ol_ImageID', primary_key=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ol_Image'


class SmsResult(models.Model):
    sms_resultid = models.IntegerField(db_column='sms_ResultID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sms_Result'


class SmsSet(models.Model):
    sms_setid = models.AutoField(db_column='sms_SetID', primary_key=True)  # Field name made lowercase.
    webaddress = models.CharField(db_column='WebAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spcode = models.CharField(db_column='spCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loginname = models.CharField(db_column='LoginName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sms_Set'


class SmsTask(models.Model):
    sms_taskid = models.AutoField(db_column='sms_TaskID', primary_key=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    senddate = models.DateTimeField(db_column='SendDate', blank=True, null=True)  # Field name made lowercase.
    messagecontent = models.CharField(db_column='MessageContent', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    usernumber = models.CharField(db_column='UserNumber', max_length=700, blank=True, null=True)  # Field name made lowercase.
    result = models.IntegerField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    resultmsg = models.CharField(db_column='ResultMsg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    send = models.IntegerField(db_column='Send', blank=True, null=True)  # Field name made lowercase.
    haveread = models.IntegerField(db_column='HaveRead', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sms_Task'


class TbItemmnt(models.Model):
    fid = models.AutoField(db_column='FID', primary_key=True)  # Field name made lowercase.
    fnumid = models.CharField(db_column='FNumID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fnumber = models.CharField(db_column='FNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fclose = models.IntegerField(db_column='FClose', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_ItemMnt'


class TbOrder(models.Model):
    tb_orderid = models.AutoField(db_column='tb_OrderID', primary_key=True)  # Field name made lowercase.
    ftid = models.CharField(db_column='FTid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbuyer_nick = models.CharField(db_column='FBuyer_nick', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fdate = models.DateTimeField(db_column='FDate', blank=True, null=True)  # Field name made lowercase.
    fcreated = models.DateTimeField(db_column='FCreated', blank=True, null=True)  # Field name made lowercase.
    fclosed = models.IntegerField(db_column='FClosed', blank=True, null=True)  # Field name made lowercase.
    freceiver_state = models.CharField(db_column='Freceiver_state', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freceiver_city = models.CharField(db_column='Freceiver_city', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freceiver_district = models.CharField(db_column='Freceiver_district', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freceiver_address = models.CharField(db_column='Freceiver_address', max_length=250, blank=True, null=True)  # Field name made lowercase.
    freceiver_name = models.CharField(db_column='Freceiver_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freceiver_mobile = models.CharField(db_column='Freceiver_mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fpost_fee = models.FloatField(db_column='Fpost_fee', blank=True, null=True)  # Field name made lowercase.
    ftotal_fee = models.FloatField(db_column='Ftotal_fee', blank=True, null=True)  # Field name made lowercase.
    fpayment = models.FloatField(db_column='FPayment', blank=True, null=True)  # Field name made lowercase.
    fbuyer_message = models.CharField(db_column='FBuyer_message', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fseller_memo = models.CharField(db_column='FSeller_memo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fqty = models.IntegerField(db_column='FQty', blank=True, null=True)  # Field name made lowercase.
    fisiteminfo = models.IntegerField(db_column='FIsItemInfo', blank=True, null=True)  # Field name made lowercase.
    fisbin = models.IntegerField(db_column='FIsbin', blank=True, null=True)  # Field name made lowercase.
    fisbined = models.IntegerField(db_column='FIsbined', blank=True, null=True)  # Field name made lowercase.
    fissend = models.IntegerField(db_column='FIsSend', blank=True, null=True)  # Field name made lowercase.
    fisprint = models.IntegerField(db_column='FIsprint', blank=True, null=True)  # Field name made lowercase.
    fiswaitsend = models.IntegerField(db_column='FIsWaitSend', blank=True, null=True)  # Field name made lowercase.
    fiscreorder = models.IntegerField(db_column='FIsCreOrder', blank=True, null=True)  # Field name made lowercase.
    fseorderno = models.CharField(db_column='FSeOrderNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fsendtype = models.CharField(db_column='FSendType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fsendname = models.CharField(db_column='FSendName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fsendbillno = models.CharField(db_column='FSendBillNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fistag = models.IntegerField(db_column='FIsTag', blank=True, null=True)  # Field name made lowercase.
    windowid = models.IntegerField(db_column='WindowID', blank=True, null=True)  # Field name made lowercase.
    billid = models.IntegerField(db_column='BillID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Order'


class TbSet(models.Model):
    tb_setid = models.IntegerField(db_column='TB_SetID', primary_key=True)  # Field name made lowercase.
    appkey = models.CharField(db_column='AppKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    appsecret = models.CharField(db_column='AppSecret', max_length=50, blank=True, null=True)  # Field name made lowercase.
    appsession = models.CharField(db_column='AppSession', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Set'


class TbState(models.Model):
    tb_stateid = models.IntegerField(db_column='tb_StateID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_State'


class TbTborderentry(models.Model):
    fid = models.AutoField(db_column='FID', primary_key=True)  # Field name made lowercase.
    fentryid = models.IntegerField(db_column='FEntryID', blank=True, null=True)  # Field name made lowercase.
    ftid = models.CharField(db_column='FTid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fnum_iid = models.CharField(db_column='Fnum_iid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fouter_iid = models.CharField(db_column='Fouter_iid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fprice = models.FloatField(db_column='Fprice', blank=True, null=True)  # Field name made lowercase.
    fnum = models.IntegerField(db_column='FNum', blank=True, null=True)  # Field name made lowercase.
    fnote = models.CharField(db_column='FNote', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_TbOrderEntry'


class TbLogistics(models.Model):
    fid = models.AutoField(db_column='FID', primary_key=True)  # Field name made lowercase.
    fnumber = models.CharField(db_column='FNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fsort = models.IntegerField(db_column='FSort', blank=True, null=True)  # Field name made lowercase.
    fclose = models.IntegerField(db_column='FClose', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_logistics'
