# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: postalcodetable/v2/city_am.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='postalcodetable/v2/city_am.proto',
  package='loggi.postalcodetable.v2',
  syntax='proto3',
  serialized_options=_b('\n\034com.loggi.postalcodetable.v2B\013CityAmProtoP\001Z\021postalcodetablev2\242\002\003LPX\252\002\030Loggi.Postalcodetable.V2\312\002\030Loggi\\Postalcodetable\\V2'),
  serialized_pb=_b('\n postalcodetable/v2/city_am.proto\x12\x18loggi.postalcodetable.v2*\xd1\x17\n\x06\x43ityAm\x12\x13\n\x0f\x43ITY_AM_INVALID\x10\x00\x12-\n(CITY_AM_AGROVILA_SAO_SEBASTIAO_DO_CABURI\x10\xd7V\x12\x15\n\x10\x43ITY_AM_ALVARAES\x10\xbf\x01\x12\x14\n\x0f\x43ITY_AM_AMATARI\x10\xc0\x01\x12\x14\n\x0f\x43ITY_AM_AMATURA\x10\xc1\x01\x12\x12\n\rCITY_AM_ANAMA\x10\xc2\x01\x12\x12\n\rCITY_AM_ANORI\x10\xc3\x01\x12\x11\n\x0c\x43ITY_AM_APUI\x10\xc4\x01\x12\x13\n\x0e\x43ITY_AM_ARARAS\x10\xfa[\x12\x12\n\rCITY_AM_ARIAU\x10\xf5\x62\x12\x1d\n\x18\x43ITY_AM_ATALAIA_DO_NORTE\x10\xc6\x01\x12\x1f\n\x1a\x43ITY_AM_AUGUSTO_MONTENEGRO\x10\xc7\x01\x12\x14\n\x0f\x43ITY_AM_AUTAZES\x10\xc8\x01\x12\x13\n\x0e\x43ITY_AM_AXINIM\x10\xc9\x01\x12\x14\n\x0f\x43ITY_AM_BADAJOS\x10\xca\x01\x12\x14\n\x0f\x43ITY_AM_BALBINA\x10\xcb\x01\x12\x15\n\x10\x43ITY_AM_BARCELOS\x10\xcc\x01\x12\x18\n\x13\x43ITY_AM_BARREIRINHA\x10\xcd\x01\x12\x1e\n\x19\x43ITY_AM_BELEM_DE_SOLIMOES\x10\xff[\x12\x1e\n\x19\x43ITY_AM_BENJAMIN_CONSTANT\x10\xce\x01\x12\x13\n\x0e\x43ITY_AM_BERURI\x10\xcf\x01\x12\x1f\n\x1a\x43ITY_AM_BOA_VISTA_DO_RAMOS\x10\xd0\x01\x12\x19\n\x14\x43ITY_AM_BOCA_DO_ACRE\x10\xd1\x01\x12\x12\n\rCITY_AM_BORBA\x10\xd2\x01\x12\x17\n\x12\x43ITY_AM_CAAPIRANGA\x10\xd3\x01\x12\x19\n\x14\x43ITY_AM_CACAU_PIRERA\x10\xe7Q\x12\x14\n\x0f\x43ITY_AM_CAIAMBE\x10\xd4_\x12\x13\n\x0e\x43ITY_AM_CAMETA\x10\xd4\x01\x12\x13\n\x0e\x43ITY_AM_CANUMA\x10\xd5\x01\x12\x15\n\x10\x43ITY_AM_CANUTAMA\x10\xd6\x01\x12\x15\n\x10\x43ITY_AM_CARAUARI\x10\xd7\x01\x12\x14\n\x0f\x43ITY_AM_CAREIRO\x10\xd8\x01\x12\x1e\n\x19\x43ITY_AM_CAREIRO_DA_VARZEA\x10\xd9\x01\x12\x1b\n\x16\x43ITY_AM_CAREIRO_PARAUA\x10\xf3[\x12\x16\n\x11\x43ITY_AM_CARVOEIRO\x10\xda\x01\x12\x12\n\rCITY_AM_COARI\x10\xdb\x01\x12\x14\n\x0f\x43ITY_AM_CODAJAS\x10\xdc\x01\x12\x12\n\rCITY_AM_CUCUI\x10\xdd\x01\x12\x15\n\x10\x43ITY_AM_EIRUNEPE\x10\xde\x01\x12\x13\n\x0e\x43ITY_AM_ENVIRA\x10\xdf\x01\x12\x1f\n\x1a\x43ITY_AM_ESTIRAO_DO_EQUADOR\x10\x81\\\x12\x14\n\x0f\x43ITY_AM_FEIJOAL\x10\xfe[\x12\x1d\n\x18\x43ITY_AM_FLORIANO_PEIXOTO\x10\xe0\x01\x12\x16\n\x11\x43ITY_AM_FONTE_BOA\x10\xe1\x01\x12 \n\x1b\x43ITY_AM_FREGUESIA_DO_ANDIRA\x10\xe2\x01\x12\x14\n\x0f\x43ITY_AM_GUAJARA\x10\xe3\x01\x12\x14\n\x0f\x43ITY_AM_HUMAITA\x10\xe4\x01\x12\x15\n\x10\x43ITY_AM_IAUARETE\x10\xe5\x01\x12\x12\n\rCITY_AM_ICANA\x10\xe6\x01\x12\x14\n\x0f\x43ITY_AM_IPIXUNA\x10\xe7\x01\x12\x15\n\x10\x43ITY_AM_IRANDUBA\x10\xe8\x01\x12\x18\n\x13\x43ITY_AM_ITACOATIARA\x10\xe9\x01\x12\x16\n\x11\x43ITY_AM_ITAMARATI\x10\xea\x01\x12\x15\n\x10\x43ITY_AM_ITAPEACU\x10\xeb[\x12\x17\n\x12\x43ITY_AM_ITAPIRANGA\x10\xeb\x01\x12\x13\n\x0e\x43ITY_AM_JAPURA\x10\xec\x01\x12\x12\n\rCITY_AM_JURUA\x10\xed\x01\x12\x12\n\rCITY_AM_JUTAI\x10\xee\x01\x12\x13\n\x0e\x43ITY_AM_LABREA\x10\xef\x01\x12\x1a\n\x15\x43ITY_AM_LAGO_DO_LIMAO\x10\xf4\x62\x12\x17\n\x12\x43ITY_AM_LAGO_PRETO\x10\xf0\x01\x12\x15\n\x10\x43ITY_AM_LIMOEIRO\x10\xfd[\x12\x17\n\x12\x43ITY_AM_MANACAPURU\x10\xf1\x01\x12\x16\n\x11\x43ITY_AM_MANAQUIRI\x10\xf2\x01\x12\x13\n\x0e\x43ITY_AM_MANAUS\x10\xf3\x01\x12\x15\n\x10\x43ITY_AM_MANICORE\x10\xf4\x01\x12\x12\n\rCITY_AM_MARAA\x10\xf5\x01\x12\x16\n\x11\x43ITY_AM_MASSAUARI\x10\xf6\x01\x12\x12\n\rCITY_AM_MAUES\x10\xf7\x01\x12\x14\n\x0f\x43ITY_AM_MOCAMBO\x10\xf8\x01\x12\x12\n\rCITY_AM_MOURA\x10\xf9\x01\x12\x15\n\x10\x43ITY_AM_MURITUBA\x10\xfb[\x12\x16\n\x11\x43ITY_AM_MURUTINGA\x10\xfa\x01\x12\x15\n\x10\x43ITY_AM_NHAMUNDA\x10\xfb\x01\x12!\n\x1c\x43ITY_AM_NOVA_OLINDA_DO_NORTE\x10\xfc\x01\x12\x17\n\x12\x43ITY_AM_NOVO_AIRAO\x10\xfd\x01\x12\x1a\n\x15\x43ITY_AM_NOVO_ARIPUANA\x10\xfe\x01\x12\x15\n\x10\x43ITY_AM_NOVO_CEU\x10\xf0[\x12\x19\n\x14\x43ITY_AM_NOVO_REMANSO\x10\xd8V\x12\x1e\n\x19\x43ITY_AM_OSORIO_DA_FONSECA\x10\xff\x01\x12\x16\n\x11\x43ITY_AM_PALMEIRAS\x10\x80\\\x12\x17\n\x12\x43ITY_AM_PARICATUBA\x10\xf3\x62\x12\x16\n\x11\x43ITY_AM_PARINTINS\x10\x80\x02\x12\x13\n\x0e\x43ITY_AM_PAUINI\x10\x81\x02\x12\x13\n\x0e\x43ITY_AM_PEDRAS\x10\x82\x02\x12\x1c\n\x17\x43ITY_AM_PLATO_DO_PIQUIA\x10\x82\\\x12\"\n\x1d\x43ITY_AM_PRESIDENTE_FIGUEIREDO\x10\x83\x02\x12\x15\n\x10\x43ITY_AM_PURUPURU\x10\xf1[\x12\x19\n\x14\x43ITY_AM_REPARTIMENTO\x10\x84\x02\x12\"\n\x1d\x43ITY_AM_REPARTIMENTO_DE_TUIUE\x10\xf8[\x12\x1d\n\x18\x43ITY_AM_RIO_PRETO_DA_EVA\x10\x85\x02\x12\x14\n\x0f\x43ITY_AM_SANTANA\x10\xed[\x12&\n!CITY_AM_SANTA_ISABEL_DO_RIO_NEGRO\x10\x86\x02\x12\x17\n\x12\x43ITY_AM_SANTA_RITA\x10\x87\x02\x12!\n\x1c\x43ITY_AM_SANTO_ANTONIO_DO_ICA\x10\x88\x02\x12$\n\x1f\x43ITY_AM_SANTO_ANTONIO_DO_MATUPI\x10\xf4[\x12\x17\n\x12\x43ITY_AM_SAO_FELIPE\x10\x89\x02\x12%\n CITY_AM_SAO_GABRIEL_DA_CACHOEIRA\x10\x8a\x02\x12\"\n\x1d\x43ITY_AM_SAO_PAULO_DE_OLIVENCA\x10\x8b\x02\x12$\n\x1f\x43ITY_AM_SAO_SEBASTIAO_DO_UATUMA\x10\x8c\x02\x12\x13\n\x0e\x43ITY_AM_SILVES\x10\x8d\x02\x12\x16\n\x11\x43ITY_AM_TABATINGA\x10\x8e\x02\x12\x13\n\x0e\x43ITY_AM_TAPAUA\x10\x8f\x02\x12\x11\n\x0c\x43ITY_AM_TEFE\x10\x90\x02\x12\x17\n\x12\x43ITY_AM_TERRA_NOVA\x10\xf2[\x12\x16\n\x11\x43ITY_AM_TONANTINS\x10\x91\x02\x12\x13\n\x0e\x43ITY_AM_UARINI\x10\x92\x02\x12\x14\n\x0f\x43ITY_AM_URUCARA\x10\x93\x02\x12\x18\n\x13\x43ITY_AM_URUCURITUBA\x10\x94\x02\x12\x1a\n\x15\x43ITY_AM_VILA_AMAZONIA\x10\xef[\x12\x1d\n\x18\x43ITY_AM_VILA_BITTENCOURT\x10\xfc[\x12\x1d\n\x18\x43ITY_AM_VILA_DE_CAMPINAS\x10\xf9[\x12\x1c\n\x17\x43ITY_AM_VILA_DE_SACAMBU\x10\xf5[\x12#\n\x1e\x43ITY_AM_VILA_DO_LAGO_DO_JACARE\x10\xf7[\x12\x19\n\x14\x43ITY_AM_VILA_LINDOIA\x10\xec[\x12\x19\n\x14\x43ITY_AM_VILA_PITINGA\x10\x95\x02\x12!\n\x1c\x43ITY_AM_VILA_RICA_DE_CAVIANA\x10\xf6[\x12\x18\n\x13\x43ITY_AM_VILA_ZE_ACU\x10\xee[B|\n\x1c\x63om.loggi.postalcodetable.v2B\x0b\x43ityAmProtoP\x01Z\x11postalcodetablev2\xa2\x02\x03LPX\xaa\x02\x18Loggi.Postalcodetable.V2\xca\x02\x18Loggi\\Postalcodetable\\V2b\x06proto3')
)

_CITYAM = _descriptor.EnumDescriptor(
  name='CityAm',
  full_name='loggi.postalcodetable.v2.CityAm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_AGROVILA_SAO_SEBASTIAO_DO_CABURI', index=1, number=11095,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ALVARAES', index=2, number=191,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_AMATARI', index=3, number=192,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_AMATURA', index=4, number=193,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ANAMA', index=5, number=194,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ANORI', index=6, number=195,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_APUI', index=7, number=196,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ARARAS', index=8, number=11770,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ARIAU', index=9, number=12661,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ATALAIA_DO_NORTE', index=10, number=198,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_AUGUSTO_MONTENEGRO', index=11, number=199,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_AUTAZES', index=12, number=200,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_AXINIM', index=13, number=201,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BADAJOS', index=14, number=202,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BALBINA', index=15, number=203,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BARCELOS', index=16, number=204,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BARREIRINHA', index=17, number=205,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BELEM_DE_SOLIMOES', index=18, number=11775,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BENJAMIN_CONSTANT', index=19, number=206,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BERURI', index=20, number=207,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BOA_VISTA_DO_RAMOS', index=21, number=208,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BOCA_DO_ACRE', index=22, number=209,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_BORBA', index=23, number=210,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CAAPIRANGA', index=24, number=211,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CACAU_PIRERA', index=25, number=10471,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CAIAMBE', index=26, number=12244,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CAMETA', index=27, number=212,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CANUMA', index=28, number=213,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CANUTAMA', index=29, number=214,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CARAUARI', index=30, number=215,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CAREIRO', index=31, number=216,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CAREIRO_DA_VARZEA', index=32, number=217,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CAREIRO_PARAUA', index=33, number=11763,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CARVOEIRO', index=34, number=218,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_COARI', index=35, number=219,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CODAJAS', index=36, number=220,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_CUCUI', index=37, number=221,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_EIRUNEPE', index=38, number=222,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ENVIRA', index=39, number=223,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ESTIRAO_DO_EQUADOR', index=40, number=11777,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_FEIJOAL', index=41, number=11774,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_FLORIANO_PEIXOTO', index=42, number=224,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_FONTE_BOA', index=43, number=225,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_FREGUESIA_DO_ANDIRA', index=44, number=226,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_GUAJARA', index=45, number=227,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_HUMAITA', index=46, number=228,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_IAUARETE', index=47, number=229,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ICANA', index=48, number=230,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_IPIXUNA', index=49, number=231,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_IRANDUBA', index=50, number=232,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ITACOATIARA', index=51, number=233,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ITAMARATI', index=52, number=234,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ITAPEACU', index=53, number=11755,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_ITAPIRANGA', index=54, number=235,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_JAPURA', index=55, number=236,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_JURUA', index=56, number=237,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_JUTAI', index=57, number=238,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_LABREA', index=58, number=239,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_LAGO_DO_LIMAO', index=59, number=12660,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_LAGO_PRETO', index=60, number=240,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_LIMOEIRO', index=61, number=11773,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MANACAPURU', index=62, number=241,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MANAQUIRI', index=63, number=242,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MANAUS', index=64, number=243,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MANICORE', index=65, number=244,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MARAA', index=66, number=245,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MASSAUARI', index=67, number=246,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MAUES', index=68, number=247,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MOCAMBO', index=69, number=248,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MOURA', index=70, number=249,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MURITUBA', index=71, number=11771,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_MURUTINGA', index=72, number=250,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_NHAMUNDA', index=73, number=251,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_NOVA_OLINDA_DO_NORTE', index=74, number=252,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_NOVO_AIRAO', index=75, number=253,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_NOVO_ARIPUANA', index=76, number=254,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_NOVO_CEU', index=77, number=11760,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_NOVO_REMANSO', index=78, number=11096,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_OSORIO_DA_FONSECA', index=79, number=255,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PALMEIRAS', index=80, number=11776,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PARICATUBA', index=81, number=12659,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PARINTINS', index=82, number=256,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PAUINI', index=83, number=257,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PEDRAS', index=84, number=258,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PLATO_DO_PIQUIA', index=85, number=11778,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PRESIDENTE_FIGUEIREDO', index=86, number=259,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_PURUPURU', index=87, number=11761,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_REPARTIMENTO', index=88, number=260,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_REPARTIMENTO_DE_TUIUE', index=89, number=11768,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_RIO_PRETO_DA_EVA', index=90, number=261,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SANTANA', index=91, number=11757,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SANTA_ISABEL_DO_RIO_NEGRO', index=92, number=262,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SANTA_RITA', index=93, number=263,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SANTO_ANTONIO_DO_ICA', index=94, number=264,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SANTO_ANTONIO_DO_MATUPI', index=95, number=11764,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SAO_FELIPE', index=96, number=265,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SAO_GABRIEL_DA_CACHOEIRA', index=97, number=266,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SAO_PAULO_DE_OLIVENCA', index=98, number=267,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SAO_SEBASTIAO_DO_UATUMA', index=99, number=268,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_SILVES', index=100, number=269,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_TABATINGA', index=101, number=270,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_TAPAUA', index=102, number=271,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_TEFE', index=103, number=272,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_TERRA_NOVA', index=104, number=11762,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_TONANTINS', index=105, number=273,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_UARINI', index=106, number=274,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_URUCARA', index=107, number=275,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_URUCURITUBA', index=108, number=276,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_AMAZONIA', index=109, number=11759,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_BITTENCOURT', index=110, number=11772,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_DE_CAMPINAS', index=111, number=11769,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_DE_SACAMBU', index=112, number=11765,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_DO_LAGO_DO_JACARE', index=113, number=11767,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_LINDOIA', index=114, number=11756,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_PITINGA', index=115, number=277,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_RICA_DE_CAVIANA', index=116, number=11766,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_AM_VILA_ZE_ACU', index=117, number=11758,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=63,
  serialized_end=3088,
)
_sym_db.RegisterEnumDescriptor(_CITYAM)

CityAm = enum_type_wrapper.EnumTypeWrapper(_CITYAM)
CITY_AM_INVALID = 0
CITY_AM_AGROVILA_SAO_SEBASTIAO_DO_CABURI = 11095
CITY_AM_ALVARAES = 191
CITY_AM_AMATARI = 192
CITY_AM_AMATURA = 193
CITY_AM_ANAMA = 194
CITY_AM_ANORI = 195
CITY_AM_APUI = 196
CITY_AM_ARARAS = 11770
CITY_AM_ARIAU = 12661
CITY_AM_ATALAIA_DO_NORTE = 198
CITY_AM_AUGUSTO_MONTENEGRO = 199
CITY_AM_AUTAZES = 200
CITY_AM_AXINIM = 201
CITY_AM_BADAJOS = 202
CITY_AM_BALBINA = 203
CITY_AM_BARCELOS = 204
CITY_AM_BARREIRINHA = 205
CITY_AM_BELEM_DE_SOLIMOES = 11775
CITY_AM_BENJAMIN_CONSTANT = 206
CITY_AM_BERURI = 207
CITY_AM_BOA_VISTA_DO_RAMOS = 208
CITY_AM_BOCA_DO_ACRE = 209
CITY_AM_BORBA = 210
CITY_AM_CAAPIRANGA = 211
CITY_AM_CACAU_PIRERA = 10471
CITY_AM_CAIAMBE = 12244
CITY_AM_CAMETA = 212
CITY_AM_CANUMA = 213
CITY_AM_CANUTAMA = 214
CITY_AM_CARAUARI = 215
CITY_AM_CAREIRO = 216
CITY_AM_CAREIRO_DA_VARZEA = 217
CITY_AM_CAREIRO_PARAUA = 11763
CITY_AM_CARVOEIRO = 218
CITY_AM_COARI = 219
CITY_AM_CODAJAS = 220
CITY_AM_CUCUI = 221
CITY_AM_EIRUNEPE = 222
CITY_AM_ENVIRA = 223
CITY_AM_ESTIRAO_DO_EQUADOR = 11777
CITY_AM_FEIJOAL = 11774
CITY_AM_FLORIANO_PEIXOTO = 224
CITY_AM_FONTE_BOA = 225
CITY_AM_FREGUESIA_DO_ANDIRA = 226
CITY_AM_GUAJARA = 227
CITY_AM_HUMAITA = 228
CITY_AM_IAUARETE = 229
CITY_AM_ICANA = 230
CITY_AM_IPIXUNA = 231
CITY_AM_IRANDUBA = 232
CITY_AM_ITACOATIARA = 233
CITY_AM_ITAMARATI = 234
CITY_AM_ITAPEACU = 11755
CITY_AM_ITAPIRANGA = 235
CITY_AM_JAPURA = 236
CITY_AM_JURUA = 237
CITY_AM_JUTAI = 238
CITY_AM_LABREA = 239
CITY_AM_LAGO_DO_LIMAO = 12660
CITY_AM_LAGO_PRETO = 240
CITY_AM_LIMOEIRO = 11773
CITY_AM_MANACAPURU = 241
CITY_AM_MANAQUIRI = 242
CITY_AM_MANAUS = 243
CITY_AM_MANICORE = 244
CITY_AM_MARAA = 245
CITY_AM_MASSAUARI = 246
CITY_AM_MAUES = 247
CITY_AM_MOCAMBO = 248
CITY_AM_MOURA = 249
CITY_AM_MURITUBA = 11771
CITY_AM_MURUTINGA = 250
CITY_AM_NHAMUNDA = 251
CITY_AM_NOVA_OLINDA_DO_NORTE = 252
CITY_AM_NOVO_AIRAO = 253
CITY_AM_NOVO_ARIPUANA = 254
CITY_AM_NOVO_CEU = 11760
CITY_AM_NOVO_REMANSO = 11096
CITY_AM_OSORIO_DA_FONSECA = 255
CITY_AM_PALMEIRAS = 11776
CITY_AM_PARICATUBA = 12659
CITY_AM_PARINTINS = 256
CITY_AM_PAUINI = 257
CITY_AM_PEDRAS = 258
CITY_AM_PLATO_DO_PIQUIA = 11778
CITY_AM_PRESIDENTE_FIGUEIREDO = 259
CITY_AM_PURUPURU = 11761
CITY_AM_REPARTIMENTO = 260
CITY_AM_REPARTIMENTO_DE_TUIUE = 11768
CITY_AM_RIO_PRETO_DA_EVA = 261
CITY_AM_SANTANA = 11757
CITY_AM_SANTA_ISABEL_DO_RIO_NEGRO = 262
CITY_AM_SANTA_RITA = 263
CITY_AM_SANTO_ANTONIO_DO_ICA = 264
CITY_AM_SANTO_ANTONIO_DO_MATUPI = 11764
CITY_AM_SAO_FELIPE = 265
CITY_AM_SAO_GABRIEL_DA_CACHOEIRA = 266
CITY_AM_SAO_PAULO_DE_OLIVENCA = 267
CITY_AM_SAO_SEBASTIAO_DO_UATUMA = 268
CITY_AM_SILVES = 269
CITY_AM_TABATINGA = 270
CITY_AM_TAPAUA = 271
CITY_AM_TEFE = 272
CITY_AM_TERRA_NOVA = 11762
CITY_AM_TONANTINS = 273
CITY_AM_UARINI = 274
CITY_AM_URUCARA = 275
CITY_AM_URUCURITUBA = 276
CITY_AM_VILA_AMAZONIA = 11759
CITY_AM_VILA_BITTENCOURT = 11772
CITY_AM_VILA_DE_CAMPINAS = 11769
CITY_AM_VILA_DE_SACAMBU = 11765
CITY_AM_VILA_DO_LAGO_DO_JACARE = 11767
CITY_AM_VILA_LINDOIA = 11756
CITY_AM_VILA_PITINGA = 277
CITY_AM_VILA_RICA_DE_CAVIANA = 11766
CITY_AM_VILA_ZE_ACU = 11758


DESCRIPTOR.enum_types_by_name['CityAm'] = _CITYAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)