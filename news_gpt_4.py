from pyChatGPT import ChatGPT
from test_api import *
import time
from pymongo import MongoClient
import urllib
from dateutil import parser
from datetime import datetime, timedelta
# from timeout import timeout
import errno
import re
from steamship import Steamship
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..5N_wFUO04RsWirZ9.QbeljngHxD9SsfItY6YsVgi8vToAgth32PdAnNEaP_FJAzItAUkCdWLSIfycvxHqYVjBflCaf-IWFRbySkMlBpMm77BRXmW0FkEyaaFIKE9RtIFEZ7SJSsh2QFlHUie4doJQXxQdmSgFIRO59--HQVPYXu9Xcy1lwQu70tXn_3E46YULSgUwsCdLlmO6aLLGBF1Hq7qWfjgu94tLX4ff37WJdqpj-llbp0EwFzZkPU4Q_HQWh4l8Sv6835gce3lHXPsTMzOMztuS2H070navnQE-sfDM7IXZk7ueVd208VJILg8CZMcuU4rh76EjrvYKoUpKUcrL_uJ9zchdkIxZriKCuTEaOAcjgkB5JsARTZvuGqzZHG-tJfBaRdqyUt43wc7pirwFopqm8oBSszi9cuDlHkFJcAfJ6l2PQHkA2boNxxr55xTQU09CkuKOn9GjoPS-11Qo8_lvAt3UVU3r_QHN_dOjGtfK5yHwheLv1Rq-S_g7hWl_zSlGVS7mvuOw0fNseYdK0WrS1Yu9FyQgw_Jv5zZtf3rMjXvzoMRDOkOg5L-4SHUC6ZZUpnwCABYBlDZMjAe9SdVY1vvXE1buvumeQUux9GWSPMScwbb4Kutv7D66vpieJWiahQ4bvKjMgTLxWOGEIYnRHm_SzYXYF1VClWsadGqn7rNrN_rX_EqU_CY9Ww3X8i38KrPAAYspLy9AZ_6PIVTUeNT67dawf4Fqu54taAFpQajB8QkCC6SUJdBo7yGFnBceKZh5F3vV26GkzEoRfU8TG2PConKBV2gHXaSREI-EL7SstwdF7ALpBILqpjJ8SjagxtaY6d6tBtwQDU8p4UJ527U15-5AUvJ5md5voGWBqTBe-QOxaxpN4DB5rpTi1LRfKugCOv4o-q5LSUXPx2aEYz64DDCe-if368BN9RArl-KyBImR42V6OOKdtZ2unMb5IbjY9jHA2bo5OXgvOWVhpI1rnzTy-OgU1H4Z8PmTEoyF5eCHW0OXP8M4U-WCgG7K2DsALpClAkIekGIIHo729VYLyQaDugUYPfXxbLgnvuzqHHIBtlqIg5yapgy3OsB7mozm2jfXMK_ThDRz4m7QyufEIyDZmA_myS_4L27m7qR8htJz7-Tv4TDuiKl-4RRiv3oyfyZ51pyJsVzb5_Z3o6th_WUkJgvGWkG-HtMPJRm7sBdB3YKBd_m-xv0KXb0hkQRCTqDrfBXwLVbMRNqwnr5QPoZV0vM1LLG0l4HwTdAJYKNcEhqrNqXANOwGR2XdgdYdvn8OcH-f5ENoLa0N3niE-yblxrnHZ69QCRhz-50uniUsgBL5P64gKJGJHD9ILuvJl4cjStwXG9H0B1LOtSRipiXm62UkUXa0VgEjhBStAvMOVagEOJzPNb5HVMThDj9VBfSyHEGMW3tKOu388hJMLfMTl_S6Q35j3HHMThmHtRTIKzLqxeNO_MsVZgmeT0ve6l62KplM4sV4WpzgPYCOYFi1pRx8tnGAz2Jl1Atnr2JKiOUx3K7rwbWGv6Na03GIOA_VtAi4vMU45b4X4GRpauzzkT1WPowRKaxhmrARgguMd7CJpXRfgD99HFrAx0cMPBoQtwlOF0PV8x4Dhcwnbdd4utEomLOak_-Du6Pl1zFwNCD5NGUO-3DQvYgerdd7H-cYAeSvIe96u35U3iEoK1ZNmH3rZBk13o5WgyETIBIts6B0fKBVr26Eu6ou_--VoIQuX1G8VbZLZ8ol6cfN2LyiY8BejNFpGVLQLLju4wSVPgPB8nIn1whEVjGLXMt0qzdpFdeYkpflgn5DlYO-xDXxwkMOaxGFnTj-NYe6Pq-HufAnQBMr7A6Igx8D1kV5mzFGvnyHvYU4gKJ_x_03ezEMcSWQnhPrwBIKW_K1WgflN_vi2uOIWeZg4qGDaToredplUJpPvz5rLrMZ8xq6h4wLih6RgUY72RrTSO_RHOPBYGQne1G1b_1pv_dCuNVzfD5hksH6YRX6k7aFc3l8z-T-qQDxSGCc8jXBlFTYgk-B-Izj_1zR_SP7_J8VSXc5MI7tk3XxZTKwfTjjZm_zTq9dHnALaA44XDJ8m9sNOC82uoKJ8nFYtWTLa_xVz5ZMNIze5z2Bmwy9BxlcyNPQEuHhONYpvyj45Q3ihlzNk5Ph0p6An7rnqCaCmg0n-tVOynrzOxhHwLXyuYVFKLlJJvaipObSNY7MuHogfdpqb2t0EyZt-StlpOe5bPy6XyaqLJZyzOlaOrCpPBPfQRAmjzP0WKAUxvl0OSG-WG7Tq5jd-nvJBhvChSRZMG3xyNj67_s-UAtJPeK8UI234ftHhthCoSxTDP8WFC3852O_KGqKRU4vjXXVLNnZCfFrdbftu-RR7Srieak89C-9sX20wNLtMWt8_cXdfA81aV2cHIugrX7QdkN-iOf74CdYItmJKup8qRvUoDbNAw0iraELTyI6Tv-1V208P9fiaMx1Y7na0X-DSId8YBi21grDRhpcbIapuepuEfaOd1uTzwfWCY_XibOCwVNylxLO-rVcfbbO50mhf4I-3gYIchzZedWNM9sYkIK-4VC1ZWNex0jxHPM1Wul1bjffbhAOudm8UyiSngyxtdiF5p7PmPgyMkUibMBAAO9ZWuXKBNHlZO3YN28F53Jl-giBz2N-aZ0iylepHUm3u5lXPPsk0C6k3aM.HMK3QFY9ucokfnaypzRRtQ'
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0IMykT0A3yHndsRk.feUyXpFR-BuTM0FClD5lKXLQDgPmh9tn7wcJ0Gis4aSHRYnAjsxyXgHwBwYoTbNUB6AUPr8SNqIBpENlZ42NI3cWmuq0FhmhxKbpMnK3tdX4cfDu0PN_4t_3J9yZSwsvLcDOIkEcDpNADxYl8Kqfw5WiKOmEgKcsaTUfZbPzMZcpQHS1c44L4PZjtK19xmxJcozB4YobO5MaOTjaNqD0GxU2Id4kV3SjHaRbick0wtvtAxvOIjgdMQPal-9amXfcfdEBjn9upAZQKRVRORpBnwK5Z4_Tm4VMNCEVw9FZ4j0CJJZlqhaBgfQNArhZpNiAT5Iz-aI84-ArIpeFMj02Tldf8tMXelIwqkh7QeNc9ltIzUdB8Ohwv4uVM4q2Xa6XTbMOPuD7_72tVuIBWG9p6B24B3FqVToZQPnJtptVo_Vd947lIUwHIglu7CyVP1Ioe-6pLjhWReP5N_fhOqfC6WJPYhntTetVriQrMyNHI7l4w9s4jgCqyOgZf8F_6avY-sMw8xfR1MvSyzKtwarzn0aDIs-LwoL5hd5IhdNpCD19pQEoocba1LwGD5--Ijn4gfAohU77u7bMMPz5dYKoL-CiqCMS_Vr2UpjJvw-m_eJb3yqgWqWsr8DhEVNfEvegtzYthBFcNQW-8YdHNSwwJVeXnPZjrhrralIuCPCavIFsituDTGLwiuw4Tdr_u9drasud0TnAQtwhIZ5REaMi36aILQLWgsbSUE1q-kAstHI-Ibmfd95gcKyH_lmCvrNELsAf09UzV_xOzezlWciCCnG9X-prCFt-gnYcnxxsh1l4pBaRmNfzle63z1UD-FjWKx14WjR_VTs5p1ysPB6ahil00HNMoFzkaDzjQtSpOBzpt7_PiQfa1_fE3NtlqeupT_K1FYLeLUFh-dT_5dcgYx8RVSDt0ZsfdONbJKgbuIeWbDBfA08eYZJPEx1la4XVccKil1PxNbqrBusOSz8L6MC9fp3rMdQgkbriOPWqQ1mr8G0W1Ow8QZt3atpmTs5L2aT8CviLZK2ZPPVlsyN8nJN5UJp0E1aWyllKBgfhuvknnr99OCHgB7i5brxNS-wxdYG1F5IdJYN9qAdNXqpItC92JWnTA7tC8X7YToBmxfDoxO_gzJHydLatgAPFltZ44F1FPlYA2CT2lTXMyOATr5x0jWa0VQmcMgsPdSUJD2MBzaO79e_vBGiJFd_h-NgrXOeOQ5GK2wfdHQNNToItBor1_YP_mhNBl8hH_GdwaWhdZLtjUm0tHh08yfkjDvLawnqAfMPuAPI8UrEyqvp-_ZgjJOQSficgztxAvvgnIGDhRxesWUUKLk5o3c8UcMfS_lGnBbA_yN3w4xfzJIYNsCZPdynXDfb2ffuF7iG2LD0q5v7Uhfo54Pq166SiXhyVffKoQi8q7Xdu56vIwm-EWtV6SdRpIsFC-GGGVJiQvG2e8L3LA2CBQWCaYC26RvX6s09aE6_C8mLpY_m6wziueX1vuMasQb_SQ2AkQiYi0vR6cIpbRtIFIU214X_NE6v0wnYu0ftqJa3uXtitZMWSx7few68hdRswQKJJKLE8txZLnuD-5VxNKFXWdi3iOvl4h5baArVCMQEWosoN828UM5WejfhjuIR7-mlQzQxgKxk8-rJEpT5QlvnxuHmQil6NAxXymLe7KePGJocWf3hdhpaR3KP81Hx7DHu99ah1FcbqL5Mq19Cg7eYumO0NvxaMQxnKeT2H7ZFnOa58U6D1QK-rwsVJOzRPAvTjCjr-75X761xmKD-k9H7ejutWoB6tprwNXc6LqQcD1-QPr9oygCGHKFw6IYQzMq7v1n0KIY6IHiFe40-8dI8NfFjZWUmAam2UeBTcHO0W_rWCZ2tWtibLmmMCqX1lB8QBoJ9qfC5xzvS9dPJfpsiTKJyyX2mG0K1lKUQgLzff0qXPAhYewD_lwrkkdt40FABCVtaw23KryT5FO414SvTAQ3pIFnMm355sDcACg03qR_F5pffWwEg7VCalmk3-6a5iWqjR3WtF9_Lvmo48ubBMJnh9-AtH_4UE7E1ZHA0M8RFAKqtjf0xuJnp4J4atFPr_TXRycVVRgvyBW_Peg6dVJjii1a4Jql5jaZrAOH9t7iAGYY_LqiWsnuXDIlbmB4lYQfRWsPoWYcAznKb7HYhqrhwAMlC3m9w2Uvwmjp0ftRDu1q3h5_JFaFruPjqxWFk1-IcY3shVOqt4GJAu7WmUX-0QruWjRyWaxNe5BoIpvWu1-oP4PFSAAPcVqWznPrC84b-JroRnBusvLICSEyWymgZgiuJtBYw1vgt2dzItW7uLme8zozE6impIKD2jU3R6vYDS2s30yMHdQUfcFdei-v7EgTvTG82yBkyXIycTX-sYza8XhJc4QEizITkB0yVsHT9vQq2I1ADbx-6t2hC3ZgAnW4xi2fiPitCveN1_qn-3ejSo_jsnpch-AYfvfPNXmPPU0Vc33wUZEwEnZaZkw9CmJmMoOenISBqqh4yYmLEEOrdgXjpPZDFkZPSOQhqYj9NkaHTNO_UyJcWm0Z5RrQz4hPphY6YW_jo4oUHBWqOOkMP00YADVUvjAdKGgxAoplf1DnmgxR-PZejQYTIMFzXAWRKtKJU1LC3P_PyKrjjwd55fFVmw0n2rjl1cBIcT6Cs3n5_J.5Wr0_3owBQvCtwVPOdqjrg'
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..oa4LBFVNAddGeZNe._5zbE9HjhkzTd2cUou6AsWEBkaLsK0lByWOO8HARJV9motBD-_DIFAQn9WOFZYhrmE9h_C-NrObMTyD7FBMnp5tHe4os58umHufzKAiMkuntiZEfEuFLS7KMxtFdKH9fsiQi5bfwFmqMRRHlP6Qt3er2JiNtl1gtFJjhVHa1hc2bFVryWwWsQw9QJl1MexqToTty64vQAmFXzwEnbRrHTQMze52FUYkYdxhJzgpUoWm_6SEwaVYX-mmAdvHO_Q1UM9ZPzYp2L58l5O0Fned3KpjmrFQ8PkjHLzKkoEg-pQnbB4vDfG-DhXaCStK7gpjGfzyV_1PV1QeW5UEdax91877GJuNNssYDLlYn4_xQxGCAXoneE5iuLYWlZxLTYPRX288Z1B5fEO_5sougXSFICUwgnMvg05y0s41AseRADQAYDsGQ46zpNcPXtPJGxV1Ua1HQYCCpbN5fOnEobygkZSPPzrU44c6F-yarWd1p9QfDUN0TdEc7NI_ok9SGW1VmD98cAAaxyXma3vHkwWw9XzrQzJK5aSGl73oNLxY20d7LQ3s79-h03tGFsqC0CkvqccKZZEy7-12RHweqZGEjLSt0ivZ3XvYyPKHjDlhXijTs9WsMExghyHO2fKV_moSZ3x6pfNRG1TIAA3RvqPcu6S3Eex-hWsdeWLDiHdTVWHpkQrA9Zj9v9O-E0tAWoDlu_yCCEbU0YgiCveNZWXRt0rRwZMVeOkqI908DxrQpNCyeTFOUAXEDtzFLBANEuXELYCoa-VqlUBHE0crou3Zp98DvsJz06pbLZWtlb6xOrzl3ahaiy1VsgDz_1hSmn7d7khJX26WrD0lW7MZp1ecxaQ_R-3A1566o4mqXAv7iCpEIXIG3b_3n8-ZwAo5D0OXpAArC3GgRHR4_m092nhGNAuHww1HcXJvdpZqJbd6yP2vkdK-TiTevvuUQqDznK6sFyR5Y_wX3KuhsGJTOKbHUWei2E7oy6BlJMiGWozKV34on9EsQsWz_IZTukqcSV_soAtfAxclUUNvgp_pRJs7G7CdtoO65JlGjNWE2Q0w3uIGg531GGIsjoI26fjowFicrOECnBSQCIceHI0AK0Y4UmWLpUcImblpmg_rTxTKQgEYlCliAHifLmkyKqq3TQJvgBJ_KqTXhI5nJkCH-Fh7Q8Rnjcm_sxxP2Cv9j6CHhJMXKNLPs5gCHt0JAlR6ppOl5TwsNOptPkLMjviYyaQkyGOhq2wYekSVHp0r-oxBaBlEjDHSlLAOIC6zv1Cbv97Ebq1jciA8QcbWxe5RUUYYC-scpEI_JaBV8Qc0dkw6DCf09vAtB2te3VYtbKvui5tCYXa7gCcLHTNfRsBpqHkMuJ4cPm6LQ8A7I0ejPdj8HWJjgPles_NpD2krcsdObQ2hbpRoMclkNcVMm8IRJSX9YjK6XJliBYhFPGOFS6aI-aupjjxFVe38tK_C7avErhIwyhCLyl88Op7aF-A2lMdRETCyB014bLQaNQhf771BdpN783BTDRQVwvlLliM2N5kDQZ9lESG70AltZ1BvMd200qmNV1T7o2cdPvd3X6H4ZCk9D3BFYHuWeC7imuXa8MSA14OSB6P60HsykXH3L2eHe2Ix2ZjEu48ToXKqg2MZl-1DZDu6TMwpnkU1EiatRJWDkA8m-AKrR-7LcrhmhQtUEnMAZQm8UdJTjVraTJw5_Bzxmed0YtEMQxbZJrCxf_IWYqFFfer01TN1zhensCBhEY4FKUj5DQ58sci9i3-kLlQWy_P8JXHzrf2lXs-wENd8S739pGs3Rk7LLJkbMwOAdn0wc25P3iVw4xXyl8w-acsZMvxznutEJtKa-qdzjgEuLjKl4IAKin8ZYpDtKyh9gUn0hSW6H-3CDk1lt8y91yILYbDUporsUv6iDpxjLWgHB_VPHgktrBJxMSJOQCcMH4E9euFYspc0cvWs4pn4-rbIoyi9LtQvg8MniS9XhfzsGPsjCVuHXTEj5ASEKTG6yDmv9_lWj8fXw1TkioJxcB4zTYMyFFioqyijNxNhy44wZMTVWMND7gqcy5IGhg8ynNo8nDMw9IoSDO1nL1_ENlNmvLpU8yM7sE0sM4OLTC2-fUurxs0KKrOA3GqMkGb-VKSV3dprAPHQxtTThC5ANKUoT6ShHD_d1igTDpiRQPnlFbPn8JCyJw0Bcnr3wOwoQFm2BLtYQk12DTm8TMWLEXDWn1JUGK4MC-9myBZWLmIAgmqnxrDFvvYf_bZBZ1SUgI-ZZvYha6uRR8rj669Yj_YjGKvd8xNCKcD81M5nOxektaRjGof2XfCSQHLQPlb_kWjdhHfl748blHMhxaJyuMD7c86hD4wQlK2qmEI7uq9BIetSmoyWDQuXI0uo9HEAMcrNwLHMCb7yLiTdk9v7M4mIxp2b8LJopHUygbGvXJVmFzDdmCHNnr_SEjImVMdmeZleiIeBx-elhq9fhYhoT9-CtFLYz31xMNcccCbJBj5NyCkj1cjg1B3L9jW_Y4RL3oKFkAfR50qcDMcQIoyZOFYh9PcAKwNnomdaPVuNnCRJ544qoZVXazMiHeEOfLRs5-pfPGIwvBwfXVw31rwf9VKofBHY9YHe8pNGx0ttoZyoOIC088tfjbCSQ4ZUjrl0v1hG-9zDxXV3iEy6KyBMMGiv2.ihkxAZXD8DHKFCBsAtFbPg'
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..YZPbKxFlrZFsouPC.FC_-9f1USxDK2VjawrpJ9nBWOpy0yrbnnxsf2YClvaETuIMk0bXysxwwuSHO2XFwC309Os80jT6oYvb1Hp5czTzJUbFsFHOuiYv3FtLKAF3hAI2CyrBYSHKfIa5NK_f0m7x_gpuk8iMQCW7xuv8ptzbF-VrthnD4P97-1tQn1OymmYFetanrbPsnCzZNVEwButWXLAXVRq7y9td7zvWg8tqKTPfn263I3rQNdjWrbL9gJXxMM4b2L8cStnOMHu722RT4i-pI2Y2IF019GnTGUYL6yhZrj71BsUSOnv9dr8OBYfmWxzsyeZTzpNbTMMJ0NJtufrCVN_YTxSPwqKQ3E9rx9iZAB0EF9wrhAkANczkFwx4qpzvGSwCr9ovqA_HScByK5SzU9Qfl9QkkxLmSr1mf-XvDu0k4AwPXHl_39t-PGyXdRpn8KViQqTXOdbT4I5AMXIWXH0Z-QObD5TG21TntYOCKDT_5w6uuc_z5Yq0XZGixIGMJuOYyw3mTc3lFl8Pk5-yWdTlLZqXB1D57-V6GnkkNi-2f1UlA0KqUFxdiOWVoLWHfsc89tvWiMyTS9TUOViIQZPyyw8GKwUf8U26Ik2h1O9KGKKKvlNH7v9ycBMK1WlfgTRjz1nNEsl-942w7SbXtCLr9UXiPI8NfRDuiNzJMgpIqQKm-vvJ25fp_hD5FL_9VhHoVmI7s1lIZdniilMEv8vaJzNuOGuKi8uSuJqbWVJiD-rDhgWu4uRyrdwCqivHBS1MdhSSNeIZKAUUHnsXTF_QPAUBiSg7K6Ojg-xFmL7wYTt20Jn4sj3w0buNwSEifjAi55mEtL4Ei1eQvZtmKRLCbhKl1ATwopTZOYYgdicUKogk11372a2Ogia5Box3db5w2sKqJPFT5g7Juy0IZSqTDnVRxVhykAfHofr43Z-81wHAX3MZxRkUMjMLm1UyGLF5Wgy1iZ8qHKmKfKEkn1GCx2vhGDXUvUvM1qXt0oH-6tDDCctGEx4RKoluOf9FLb3PAp34563RSmjfA2alMNPERu6u9jkoAXtv7w8pVpBV69FgMzRe7J-Eywwkp0wpcL6N6JShVMo78W4_iI7_595DAS8mfgVXiBBXbRycdECwvz4Va9Q0415QXHMU25enMSg-pybXicDkXNmD6iZrucfuwrmhwjI5eUBtAs9S3FqD923KvEVChIMnikMsvrME_4NqBVO7NRqrtWsZQPu0dUhgGM4sLU-UV04XTh-qWoZot0BBBMzInwMP5Rw4AlfzE5QacD0xze2z63JUYklP-oQClB8-_xeNxeyUacTGPTJSvquLu_tIS9TL6xgC7TiulhtOCBN6NYaSv7IPavc8mw5Hz_pKEfJZ8Da8HPORKNtE2m4vRLiRSNIO9vO8GVJuR_NCaeSnJSByUt9AzvvCQxJDYWQIx6gNYt0kptA43bCsEOjhkULCkjDBWdt_Hn-aU9nB126I90BxtPW9_ppaXssYQ9m-Rcz5BXOloWaZi7j23JK5kaPsg6I22a8fFzS0yRMxIfRtfDwEv0SgrJo8S1OXgeRyS9N8ffJ_NmiHW0T1Ok6e7eSOczRGoZP4oy-WT8roUMDzd4_ih30JMLefKDLsZGGcHgFVKWI5OVdYCBfwEUtVXN-Pwzib8CWNBTgQITbtSksAzIAHlAyMbm5bmatMJdhAmOOme-_NNz6ynba2A6l4WGAskw_-M1qLRHcoTONKH4-RsJDJeUfaB3jcohyUrZ-qGF1PQ3Dp6Y4eoO6w6sfnHseQQlQ-SnGPMAD-P0ufPngLt1kja7VjAAbg5tMBEOSsSBoFkeCT-CZ-wo7hf9HJwDKnOrz4WZcAhbtYwsQfR5tuRuR96o-ryw-ceZ7BjGHQrvpjmSdTz0TwmgfCv2aF63tOnc8yzGw-EtX3fgETCLsbZHbQaJ5Eieacje1ezpYY2X7GAlJ_TbQwqTu6HCRDwLIx3tMjfwCgItT3RO-YM42ovdgmi8nph0B4G6eEXcp5rSJbkGpm6fxClyxoZz5EjtiGLBI0g0zPzghgWbAH-kLnNm5ceQQEdp0kjxGbPKJKyHB8P_sRMu5Af5H9xWYU4RFK_sr4otJj1qXJOJat9goAXAdNwasu_rkr5th90lPzdREXOPxI7x16jA8iGtma40U3WTK9bPAy3ooG0TFvc4R0fFweEndsSGL8EB8x8gmXeI6cZ5iR8ySyqn8iRhmQcrppx3gOc57j3MQSQ7Y48r37hg0v7Ohh-WQKOOtJwb5goyL5mB7UjxHShMnss03qWEVmkLOU8jEDg_ZxK4cEm_gdVlWptfk7of-jRDSI8667J7mMNQvUUcL4bIZDHQ3crh2RAOKWTVfG_K3NreetSz81B5KNxjXAM-AUoAi0N1DnpIPSMIWU5oiQs1DyPyI8ZTLGd2HjTe7XO_dIjgxXkA3v8lEzr0F_vFpC7JlqCs5LejroNqMbO4-NKcstgTBULD-YgtV9mNHpYqjN907Yl59wOwptBUKhIsddVR8HMK9ytRE4Qq51tUsL5V0DtCcTJ2LeCAlZxSrrrpi2Mh-bLu4I-kjbs1Sc_dALJ_EXFKEtRtkWCh1jmae6dtmhmMrFBz-R91-xQc-bFIEEWJ-P6vbNhoShNM6nrI0Zp04tYkfNDT8zrt2x-LhAdy9xGVl-oaiKS9s75e111T_b-.QYvqJil-FFRWxjb7oysRCA'

count = 0
# @timeout(30, os.strerror(errno.ETIMEDOUT))
# def try_call_api(api, prompt):
#     resp = api.send_message(prompt)
all_topic = ["Thể thao", "Giải trí", "Công nghệ", "Khác", "Xã hội", "Kinh doanh", "Chính trị", "Chiến tranh"]

def preprocess_text(text):
    #Eliminated the case that "Topic: text" and "text ()"

    text = text.split(":")[-1]
    text = text.split("(")[0]
    text = text.strip("\n").strip(".").strip(" ")
    return text

def preprocess_tag(input_tag):
    input_tag = preprocess_text(input_tag.lower())
    # input_tag = input_tag.replace(" ","").lower()
    return input_tag

def call_gpt_4(task, input_text, generator):
    time.sleep(20)
    global count
    print("Input text: ",input_text)
    input_text = re.sub(r'\s-[^-]*-|#\w+\s', '', input_text)
    print("new_input text",input_text)
    re_try = 2
    start_time = time.time()
    if task=='text_classify':   
        with open('./prompt_classify.txt', 'r', encoding='utf-8') as file:
            prompt_mn = file.read().rstrip()
        prompt = "Act as you are text classify model. Hãy phân loại nội dung sau vào một trong 8 loại và không được giải thích gì thêm ở câu trả lời: Thể thao, Giải trí, Công nghệ, Xã hội, Kinh doanh, Chính trị, Chiến tranh, Khác.\n"+prompt_mn+"\nText '''{}'''\nTopic: ".format(input_text)
        # print(prompt)
    # elif task=="sentiment":
    #     with open('prompt_sentiment.txt', 'r') as file:
    #         prompt_mn = file.read().rstrip()
    #     prompt = "Act as you are sentiment classification model. Hãy phân loại nội dung sau vào một trong 3 loại: Positive, Negative, Neural.\n"+prompt_mn+"\nText '''{}'''\nSentiment: ".format(input_text)
    elif task=="key_extract":
        with open('./prompt_key.txt', 'r', encoding='utf-8') as file:
            prompt_mn = file.read().rstrip()
        prompt = "Act as you are document key information extraction model. Extracted the relevant keywords based on what seems most important in the sentence, if no keywords exist, reply only 'None' and don't explain anything.\n"+prompt_mn+"\nText '''{}'''\nKeywords: ".format(input_text)
    # elif task=="key_extract":
    #     with open('./NER_prompt.txt', 'r', encoding='utf-8') as file:
    #         prompt_mn = file.read().rstrip()
    #     prompt = "Act as you are a named-entity recognition model, perform NER from the following sentence. If there are no keywords found, reply only 'None' and don't explain anything.:\n"+prompt_mn+"\nSentence: '''{}'''\nNamed-Entity: ".format(input_text)
    
    elif task=="abstract":
        prompt = 'Tóm tắt văn bản sau bằng Tiếng Việt chỉ dùng tối đa 100 từ, không được dài hơn. Văn bản: '+input_text
        print("Prompt Abstract: ",prompt)

    for i in range(0,re_try):
        try:
            print("Vao day roiii")
            resp = generator.generate(text=prompt)
            resp.wait()
            # resp = api.send_message(prompt)
        except Exception as e:
            print(e)
            time.sleep(10)
            continue
        break

    print("Process Time: ",time.time()-start_time)
    if task == 'text_classify':
        resp.output.blocks[0].text = preprocess_text(resp.output.blocks[0].text)
        if resp.output.blocks[0].text not in all_topic:
            resp.output.blocks[0].text = 'Khác'
    
    if task == "key_extract":
        resp = resp.output.blocks[0].text.split(",")
        resp = [x.strip().strip('.') for x in resp]
        keywords = []
        for stt, kw in enumerate(resp):
            kw = preprocess_tag(kw)
            if (stt > 0) and (kw.lower() == 'none'):
                continue
            keywords.append({"KW":kw})
        count+=1
        print("Lan thu {} query".format(str(count)))
        print("result KW: ",keywords)
        return keywords
    # api.reset_conversation()
    # api.clear_conversations()
    # api.refresh_chat_page()
    if task == "abstract":
        print("Ket qua tom tat: ",resp.output.blocks[0].text)
    count+=1
    print("Lan thu {} query".format(str(count)))
    return resp.output.blocks[0].text.strip("\n")

def call_gpt(task,input_text):
    time.sleep(20)
    global count
    print("Input text: ",input_text)
    input_text = re.sub(r'\s-[^-]*-|#\w+\s', '', input_text)
    print("new_input text",input_text)
    re_try = 2
    start_time = time.time()
    if task=='text_classify':   
        with open('./prompt_classify.txt', 'r', encoding='utf-8') as file:
            prompt_mn = file.read().rstrip()
        prompt = "Act as you are text classify model. Hãy phân loại nội dung sau vào một trong 8 loại và không được giải thích gì thêm ở câu trả lời: Thể thao, Giải trí, Công nghệ, Xã hội, Kinh doanh, Chính trị, Chiến tranh, Khác.\n"+prompt_mn+"\nText '''{}'''\nTopic: ".format(input_text)
        # print(prompt)
    # elif task=="sentiment":
    #     with open('prompt_sentiment.txt', 'r') as file:
    #         prompt_mn = file.read().rstrip()
    #     prompt = "Act as you are sentiment classification model. Hãy phân loại nội dung sau vào một trong 3 loại: Positive, Negative, Neural.\n"+prompt_mn+"\nText '''{}'''\nSentiment: ".format(input_text)
    elif task=="key_extract":
        with open('./prompt_key.txt', 'r', encoding='utf-8') as file:
            prompt_mn = file.read().rstrip()
        prompt = "Act as you are document key information extraction model. Extracted the relevant keywords based on what seems most important in the sentence, if no keywords exist, reply only 'None' and don't explain anything.\n"+prompt_mn+"\nText '''{}'''\nKeywords: ".format(input_text)
    # elif task=="key_extract":
    #     with open('./NER_prompt.txt', 'r', encoding='utf-8') as file:
    #         prompt_mn = file.read().rstrip()
    #     prompt = "Act as you are a named-entity recognition model, perform NER from the following sentence. If there are no keywords found, reply only 'None' and don't explain anything.:\n"+prompt_mn+"\nSentence: '''{}'''\nNamed-Entity: ".format(input_text)
    
    elif task=="abstract":
        prompt = 'Tóm tắt văn bản sau bằng Tiếng Việt chỉ dùng tối đa 100 từ, không được dài hơn. Văn bản: '+input_text
        print("Prompt Abstract: ",prompt)

    for i in range(0,re_try):
        try:
            print("Vao day roiii")
            resp = api.send_message(prompt)
        except Exception as e:
            print(e)
            time.sleep(10)
            continue
        break

    print("Process Time: ",time.time()-start_time)
    if task == 'text_classify':
        resp['message'] = preprocess_text(resp['message'])
        if resp['message'] not in all_topic:
            resp['message'] = 'Khác'
    
    if task == "key_extract":
        resp = resp['message'].split(",")
        resp = [x.strip().strip('.') for x in resp]
        keywords = []
        for stt, kw in enumerate(resp):
            kw = preprocess_tag(kw)
            if (stt > 0) and (kw.lower() == 'none'):
                continue
            keywords.append({"KW":kw})
        count+=1
        print("Lan thu {} query".format(str(count)))
        print("result KW: ",keywords)
        return keywords
    # api.reset_conversation()
    # api.clear_conversations()
    # api.refresh_chat_page()
    if task == "abstract":
        print("Ket qua tom tat: ",resp['message'])
    count+=1
    print("Lan thu {} query".format(str(count)))
    return resp['message'].strip("\n")

def get_database():
    username = urllib.parse.quote_plus('sontung2310')
    password = urllib.parse.quote_plus("Vmagcut99!")
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://{}:{}@cluster0.gyiy6tr.mongodb.net/?retryWrites=true&w=majority".format(username, password)
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    
    # db = client['social_listening_storage']
    
    # for db in client.list_databases():
    #     print(db)
    # Create the database for our example (we will use the same database throughout the tutorial
    # return client['user_shopping_list']
    return client['social_listening_storage']         
 
def update_database(filter, collection, update_var, update_position):
    #Update update_var in update position
    newvalue = { "$set": { update_position: update_var } }
    collection.update_one(filter, newvalue)
    
def update_full(filter,collection, update_position, update_var):
    # [position1, position2] [var1, var2]
    tmp_dict = {"$set":{}}
    for i in range(len(update_var)):
        tmp_dict['$set'][update_position[i]] = update_var[i]
    
    collection.update_one(filter, tmp_dict)

def combine_analysis(filter, collection, input_data, generator, is_topic=False, is_keyword=False, is_sentiment=False, only_title=False):
    update_position = []
    update_var = []
    # if news_task:
    #     process_text = input_data['description']
    # else:
    #     process_text = input_data['description']
    if is_topic:
        print("Topic")
        # topic = call_gpt("text_classify", input_data)
        topic = call_gpt_4("text_classify", input_data, generator)
        update_position.append('topic')
        update_var.append(topic)
        # update_database(filter, collection, topic, 'topic')
    if is_keyword:
        print("KW")
        keywords = call_gpt_4('key_extract', input_data, generator)
        update_position.append('tags')
        update_var.append(keywords)
        # update_database(filter, collection, keywords, 'tags')
    if is_sentiment:
        print("Sentiment")
        sentiment = sentiment_bert(input_data)
        if only_title == True:
            new_dict = {"text":input_data,'sentiment':sentiment}
            update_position.append('title')
            update_var.append(new_dict)
        else:
            # input_data["sentiment"] = sentiment
            update_position.append('content.sentiment')
            update_var.append(sentiment)
        # update_database(filter, collection, sentiment, save_dir+'.sentiment') #
    #Xu ly xong thi cho Flag = True
    # update_database(filter, collection, True, 'check_flag')
    update_position.append('check_flag')
    update_var.append(True)
    update_full(filter, collection, update_position, update_var)

def analysis_data(database, type_app, generator, time_delta=7):
    if type_app == 'news_data':
        collection = database["news_data"]
    elif type_app == 'youtube':
        collection = database["youtube"]
    elif type_app == 'facebook':
        collection = database["facebook"]
    elif type_app == 'forum':
        collection = database["forum"]

    # process_index = collection.create_index("check_flag")
    # process_index = collection.create_index("check_flag")
    margin_time = (datetime.now() - timedelta(days=time_delta)).timestamp()
    item_details = collection.find(
        {"check_flag": False, "time_upload":{"$gte":margin_time}} ).sort("time_crawl", -1)
    # item_details = collection.find(
    #     {"check_flag": False})
    # print(item_details)
    for index, item in enumerate(item_details):
        print("item: ",item)
        filter = {'_id': item['_id'] }
        for i,comment in enumerate(item['comments_infor']):
            # api.reset_conversation()

            #Neu comment nao da duoc analysis roi thi bo? qua
            if comment['check_flag'] == True:
                #Chuyen flag cua content ve True
                # item['check_flag'] = True
                continue
            else:
                # api.clear_conversations()
                #Sentiment text cua comment
                if (comment['comment']!=''): #If comment != None
                    if len(comment['comment'].split(" ")) < 100:
                        # Extract key information from commment
                        # keyinfor = call_gpt('key_extract', comment['comment'])
                        keyinfor = call_gpt_4('key_extract', comment['comment'],generator)
                    else:
                        print("Abstract this comment because of too long")
                        # comment['comment'] = call_gpt('abstract', comment['comment'])
                        # keyinfor = call_gpt('key_extract', comment['comment'])
                        comment['comment'] = call_gpt_4('abstract', comment['comment'],generator)
                        keyinfor = call_gpt_4('key_extract', comment['comment'],generator)
                    #Sentiment comment
                    sentiment_cmt = sentiment_bert(comment['comment'])
                    
                    update_full(filter, collection, ['comments_infor.'+str(i)+'.sentiment', 'comments_infor.'+str(i)+'.key_infor', 'comments_infor.'+str(i)+'.check_flag'], 
                                [sentiment_cmt, keyinfor, True])
        # Neu chua co tags -> article chua duoc analysis
        if len(item['tags'])==0:
            item['check_flag'] = False
        else:
            item['check_flag'] = True
        #Neu article nay chua duoc analysis
        if item["check_flag"] == False:
            print("Co vo ham xu ly article khong")
            if type_app == 'news_data':
                # item['topic'] = call_gpt('text_classify',item['title'])
                item['topic'] = call_gpt_4('text_classify',item['title'], generator)
                update_database(filter, collection, item['topic'], 'topic')
                #Neu khong co Description
                if (item['content']['description'] == ""):
                    #Tom tat content
                    if (len(item['content']["text"].strip(" ")))<6000:
                        # print("Length of content: ",)
                        # item['content']['description'] = call_gpt('abstract',item['content']["text"])
                        item['content']['description'] = call_gpt_4('abstract',item['content']["text"], generator)
                    else:
                        print("Content of paper is too long")
                        item['content']['description'] = item['title']

                    update_database(filter, collection, item['content']['description'], 'content.description')
                
                combine_analysis(filter, collection, item['content']['description'],generator, is_keyword=True, is_sentiment=True)
                item['check_flag'] = True
            #Neu khong phai la bao'
            elif type_app == 'facebook':
                try:
                    combine_analysis(filter, collection, item['content']['text'],generator, is_topic=True, is_keyword=True, is_sentiment=True)
                except:
                    print("Abstract this content because of too long")
                    # item['content']['text'] = call_gpt('abstract',item['content']['text'])
                    item['content']['text'] = call_gpt_4('abstract',item['content']['text'],generator)
                    combine_analysis(filter, collection, item['content']['text'],generator, is_topic=True, is_keyword=True,
                                     is_sentiment=True)
                item['check_flag'] = True

            elif type_app == 'youtube':
                # Process lai phan title
                print("Processing youtube...")
                split_tt = item['title'].split("|")
                if len(split_tt)!=1:
                    item['title'] = " ".join(split_tt[:-1])
                # new_title = {'text':item['title'], 'sentiment':''}
                # update_database(filter, collection, new_title, 'title')
                # print("Update chua: ",item['title'])
                combine_analysis(filter, collection, item['title'],generator, is_topic=True, is_keyword=True, is_sentiment=True,only_title=True)
                item['check_flag'] = True
                
            elif type_app == 'forum':
                try:
                    
                    if (len(item['title'].strip(" ")))<6000:
                        combine_analysis(filter, collection, item['title'],generator, is_topic=True, is_keyword=True, is_sentiment=True,only_title=True)
                    else:
                        print("Abstract this content because of too long")
                        item['title'] = call_gpt('abstract',item['title'])
                        combine_analysis(filter, collection, item['title'],generator, is_topic=True, is_keyword=True,
                                        is_sentiment=True,only_title=True)
                    item['check_flag'] = True
                except Exception as e:
                    print("Co loi Forum: ",e)
                    continue
                
            
            
                # item['topic'] = call_gpt('text_classify',item['title']['text'])
                # update_database(filter, collection, item['topic'], 'topic')
                
                # #Keyword extract 
                # item['Keywords'] = call_gpt('key_extract',item['title']['text'])
                # update_database(filter, collection, item['Keywords'], 'tags')
                
                # #Sentiment 
                # sentiment = sentiment_bert(item['title']['text'])
                # # new_title = {'text':item['title'], 'sentiment':sentiment}
                # update_database(filter, collection, sentiment, 'title.sentiment')
                
                # #Xu ly xong thi cho Flag = True
                # update_database(filter, collection, True, 'check_process')

        print("Current flag: ",item["check_flag"])
        update_database(filter,collection,item["check_flag"], "check_flag")
if __name__ == "__main__":
    start_time = time.time()
    # key_infor = call_gpt(task='key_extract',input_text="GIA LAI Cú dứt điểm từ hơn 30 mét của Jhon Clay giúp Công an Hà Nội gỡ hòa 1-1 trên sân HAGL ở vòng 4 V-League 2023 hôm nay 19/2.")
    # print("Time: ",time.time()-start_time)
    # print(key_infor)
    # session = [
    #     'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..t0xlwyeOrQvsp9Ct.CcDLtTc7Uyp4I5vFxwiTL-MF8NcKzY3cNzBLHRqWjTkQga7web3BIZALlw-AW5U-3P21N-37vALsKIO5FGV4lZXZK-9QXO6E2MhdV3puPPrzI9zL3LyiRs5zPUlevhB079V2uFXqBknoi1m-uBfXe9P-t8ZC1wvNyRcA4GvC8DaoXUgHmLF7TFdHnb4rQ_SecAcddIbp6KlG_HFByd7zM-gWF-D41WTXlysVL0y0wTVFKaMiSm3bHLy3bIwyoCt6jC59hRZnFAZ95yU0IWjRfVsw6hBjKRLD6cXi8QcIHXUPpETRP-8iAW93Uv1DsElz3ieO5ZYT4kbKyy_AnUJR-gCuIj5cr4XLj5tYvwnzyudoWXVTDNSH3WUTEx8UK9RUioJNAEAjnHSZqLuJ2A-SQAf433Uh1ia0Dw8N5HrJ5VqQhlgsqjyMCAtGSB71jJGC94vn-8NI0BKMlGluUrFquurk7A5s57S9JzpJSwpyJwjqNq0LPjtZf9P55vjCx2q-HRx1QpFrvAbgd1-C4fh-kFAvKb3BUHl5usQ-9hcHeFARXME4m6-V_Ol00k9YCP5Af5bblrAgifGTgvrpUMLA3YCxJTL9xyrqCbEVXYmkUaTHotHcyAOYT7VlbZ3SyMnvN9_v9YrVtnVtCJuSUrDCNXbfeDFjZIfi0414WWj3TEQVlQysIpXxWbjJli9rXhTwo_xOc9J9O2GcPLM8qf5GbLD04_1vDvbeI_6XHfxc0_mn9nkp9zXhkwusTnH54e2jElJN9S40b443Z4pfkhg_lqZSXvmFvpvr6x8bsn1lahcR3iwPzw2lapmrC4ksMiLk4IvqlgCDZuA2IDBvy640Mf9iHlK96VVJBFrp6w8e6hGFMpOB2R62u7IXuEpPqAXgQ-jBvvOLIQG8W-oN0q-B7HbsOHM30dfVC9eCIIyLwB9lDorFQYPdANlT15H3wuw40_r_fyBuTrJEerbSfP0msCK1ezdqmy954IScDdCHN_ESEbrFBHMoBheX4qSw9vj3Yw7UBr9zIjIpc4Qpin_NV9hsWa7JEgAu0EdaRJDI_9BXmrbZo1ff_WR38j11z8V0LCNhQYFNgOXNbVGsFz7UDYt5HVMQkLx3oH1WakFnH4zBKeWPii7wjggo7nWM4AxFbtgt-JPj-WF8PhMRamGuclObffK5GJsz3kUppPI567rCFNdXV9SxIcCeJNp7PZ4m2QeLbPAY1So04DVjlZVu9gvSEgSYOZLXyfXqTCo0HjYvBY63B3YIccKATj5BFg84NVW2Ya6NVQyBk5lZrbRAyZTTyiUK6N3g9mKRc32tmwQSLEHplzxdPnjcPVeZiIl9kJEdTxjDJlBK5b-p40mGkniXWqjUVTHR6uvXUarGwgWAGeaMTlv-mUomBUUo9bO1Z0fXbkD7B1xN17yJB2jBM2D7GcwLa1cAT6yjNeVyRQBSqwz6YZwS0glgCCdnmAR4bfuYZZAgj8BxvPlZTUlH0SrAe4ajvYwuo-ZSiNYH0sMf0cO7YVHwLXEjzCGEBPeO-Iji2DEwiKoiyrKGzeQt0ZcYf7aLFloMCQsGI79ZVncl3tEJSYPYcojXPlZ9eVzG1Rf0_5gh5HOBkPpYCXRpxGLQ-Xi3OAvS13i1k9G5JbWjyQ16T_ilzYotAWFoGntAF2YWp-pcN2yK53p0OaKYqPQGvxL5O62gwGiy7Ck7BUhmyimyrkxslz7dA7BJZX7ZCZD3ZCvXL6nXN7mZR6slc9yBpcgD-otkj3HfYB94rl520_gZQwJsMRbyOOl0N0UzvG5xZ2fX0m4TNrLwwo0KCal6lraYUvl0GLBIaX6qgJqEOsJo6SalIgf51yDJgRxEU8-f_7a8O-isK2FT3m-FTN2s6nrPymb2GhItzqtC3fV-fNfEy_aCJAgygsfBJflmtebEmJxyV1nzkDXCFhoZsoOR6p0KpfQccVuDJCFfBFFiPNYOgnfDevJLgzVisPoCWNeeFkGUYNy5c1vBfwakju8Kc3-bpxgmZKmbV0dHpJ7wAMsir3bE_q20D3lYoX-IXZy5lbFR52FqGf3aa4vb3r6cfmROIGOc4_SklQWn0Wan1-SbLEBsJ87mimeZ-4NvMHwvh3fx7l1rg6hjFA68EXHiSkJZ2zdV3PrrCsvaN8yjmA1iidzxvYCi1d7IUdBrmPCnkuUL2SROST6oC5nG0gnPAJK4D8uHKrdqfgLsfTCH_B7alIVFYFCu5DZgC-tORr4OzdFWj_gV_RLvE2q76oECghzDwsH-PJ-H7V3t6RH_esI5p5TvVG356itqzfcNjPZnkAUh3qahZyy51cfVlHVyeyA3WYil66eaOEWVt264svpnfIb7d9XzrRoHU9Wo7_AoRyjyXj-AJkgmvD-R3ahQAHJBRHm0vSp8fJRndh9acTsgqU7RJhjMgyxz190HqP-e1d5LU-ZjGvAn36bSgIHPJNtwjszOw4oNBzK06IQVAWavu7uYaJ6ShVFkNIQTMc7_N1XJJy9DGVIpjwxYywm-GorXDsHvcpZPRar20GEoQxjcZG6uEMLwo980dXUQVnFBWHru1yIVga_nbzsxwRqkPhDQShO-ffgzV3YXjXmoN9Xic7-nzeAgeMIdHdB9g8ZjuXEyJd3t_4hyvnMrRBycWDjkTBWvB-P0Jtu5ZqnfMLaerPPj.2DilVPT4jECN0H7Kkek1Lw',
    #     'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..A65tzFr7SQgNNCmd.QejbkMDshVzlgigtPkOPqTAJsWhBaAFXUGR3NnIaSX_EmYSsQGziqvI91G5XmkB_raqufOnPT3EJCXKkTGeYoYTx9egBI_ScTHJo7ueu2dfI18ltYXCdhoilL2ArVyjzoXdN0CiNctX4QcCvyRLDYCiBVEOO6pZxcR5Q2SF42_-0XAH4GQh9XknDABwMmwM8wTjWYRVtowLipeg6ol0VJw7N4ksOTdJEm0CeYT124ID7asd-MzxkddmXQ4WZg4R8KQcNjDFkeWgXoTnEqO7fb8TyHMvsi7kaBZqoIGThds_vhN7ZRVXwubhCjOVtpyEYi1M2oNg5Ds-lJ3eDwycby7_1YPdUC7ga3oyaRPkriweR5R6ucKsCDcw8f9fWqxy15gFoiozJVtDEp0YVb-EjkeCkkingcqLYa_fFgkGtgv6TP4joGKNOcxp8dZ8K1F8rGGBKd-E8lKBcJ_NpiUWEKVwM8xIoFgRjxzTqfE1l7OjP3HykZCifsF5hCqJZajmyTfg2Xm1lZPARzyi1iqTVsIFBbuQU0LR1pgq25zVB0aOOmzvxwOgDRFnbH5ItxgbjjnCdCO7DA0Tmzhbi57tG-2XEckL5sbKEIdGiAQFiFf4m1OHdYMZGuvdCOA9QCrncnM3jq93jfnipowzocPRgsvHqs3tAY9MD2SZB1DKVVXtqBYx3VPCIwJb5wfokImbxzSqLtMQDhacv1FstDF1RNCBrHVfmiwsFDeTjUka1j6vpvkcOpHh9ZbwxnUoArlZRlyQxq3L2y94gD-TH9fF_DNx4WSVXiFecAEgQn9vRPUWptmxR-8A4JPLD65PsWqI2tVCgaIpS6JFuLu6md-WKeBIPrXc55BZ7MKUiszV7MU3foiMQWOvmm2agehMq_dee7N5C2T5wuI0HLYtHCnG0dUbUAFm_EKc3rd3-GTttVmiW4GmXJVdAhELXUDSQRb3D8JYSbkw5XVmpah0lrX6RJhSsAZewoM-wfXZqGHw8rNu6aVuJYRszY37RZSTo74aM-zDngus5lmCHZ6dF5RJWDUCBB8gQ1qovPIMVqvMbQCNA3tRFrNGvgmgh8Ox2_-KmXB4uzRpaqkQoJObpkLpKc2glBHUVyVitH4d3FvYW3_qLDPS_oQv45Ye2IKIM7a83yVQ1roXe8cIrwL9rWmAVhr2E5qHtZKnsNIWYA6osyE-2nRI1vFLx59qQfiBMr6xX518vv9JTrHd5CMmNb016sTwFiPYTtqh7Qny86T-WTrzEaMXzLeC-QqAE-dbSSe51vn3IuX-TTpvHLTO4T1uZAlzq8FBuDb4kRjDJ9qYb9zbve5qJ_GXpzuOjiMJyvmMBLvDcXURfo9HZS7Ms4qyDWR__kMhZejPA7nbk55oGcle9R1mXCAepLLSBSy0b3Fa4SFiQ5vyZerXIi4qslRDe4Cvldp5Fce5HExQnPrZm9JrSnN-JObkOkiKwe_szWnGz-0nlnG8yByhCVeKkGCuk-2cl0q_HEEtQuMuyGK-WWp9Wsxgn08zAWJO7X25YlyKGl47FB5AC_UApNJbulMOsKG5MNtSmL2Qy5hQOKNleY_no5G2dBdVF1JRaPIarxbBRWfoazSf-RgqRFvxsAFv1TFozoEm4Di9m_93JC93euFHr8cPbMaJ0vRh-ZFWXCb7VfvdHxxke_vYAvu0T3ykwQT29xDUeShbjrPW7vDDLzZyBWs3_YMAwdjnraWF-8PT6XXs4euXodmCqn7vPQ0co0PDBy5b7_c6m6_NfK52k-dB1rPfU3wtLY8a15OdA7-U-7ipmmxBiqqrSEgjGXT_nh_h0j_cbCHuY_gMEEa5GQPd83ll5_TNC4T7dWBV3_8MsYiioi4-Z3pzBCNy_frUYJIrx6fdSf4vP345DFrMiT_GsAZWAb05IkO0NMGHjgENnWz454bTRHp9_kALWQewxhqPoiwbiDWbM3GneDikwDIFKwMOumz3zTXXvIa7gIS1NAfYmD8PSvxj7-Z2fL3gA3AI4JxtQKZXmMnUdbFfUgNb5Rgh1l2gAydjU5MhOt2wxntwzU3REwLAtEXLav7iGo28Zz1w6ZOfq1qdTm9f3GXfdUm3nwiV_fvWblEKnoZ7SoPsoOra9zI1G64sCOHyAekaZw9mrwFcV_eh9JNDWSyOrnjwnGN4CKFazxPG97Z4EkRKV0yg54omq7uIFdR5gIc6PijCe9C5hiAPGBuoD3r1hziZapc2OVI-m9fPjZVXXdS46eXdgxWeNLxl_jWmzceM9RSSeI7WW9WCDyHYwiYLnSEG1FeQ36BTOeohoE0bMF0p-nDr0fTIO1KU8Ojl6QKuoXTCHRdPSFro236oeONZ552vFg7nQKBsQSoQSGx3a7mthpIBeRjt-Vr7dw-UbISNm6zo_6lODu7Ms6l_dCoDFMHJ7JsAu7C_AB3A44Ved98PbQboXOncs9uqoWmZrb1VqR5KieHCS0Ypf5seeljVpT9YbJNY4z0EqRHVLbzE1QpcRvATZd40ynpurXtPfzUX5y_5-jwt7fSLCw6xZuU03ji7_PKoBSmYrvElnrIAEc-gTdouD-L7Cro1ZL_Rao6r-YCJebd_cNbcjx8K6eXz65pR2GpBKmfSLcN7GI7eL7qNMxZLl4Pu1o2pRN535IS6pDo_66WqXedDCKQ.44v8BSdLTsaqm4ps7yhcDA',
    #     'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Ej5eaLcELbA7AZv0.by-DveZfkAZMirWxbTRvL23nqQl6NQdxvAeouRutQqdcXrDExbspCCTYqWsFTHyDJ1ZjcMNLW9asUvGG4vGsg-xn3UO1IBFx1X4p57mX4NSxq1QrfDFOJ5IR-n1da6ZNW_kggEseiPEkBJWTI1ipWEUvCF-6DafhKBVpyBwsNQwr0NEBuJyucbRk04uLHY4wrKEQfmiphgxsiZhmX4tCUh69C8YGKqUWFiWK_4pjmCIeLfRs1-RxgbxOL7X0u5XIt6Hy9yqsROBkYKte2aXaOTvbSzxnw0G9vIfWSKRiEWjfTOeF7NC_v3UOiGkYbnDZzgRS1o0flmBzhX9qMv67DZ484r_kSDexuUU6XetI_6aD15Pqv69NqjGFtThwGbxW9sxWLvjWfnjLhiriMSE2lS6HGE_2DZronj4dAfBuHTvT8BIlb9s1TVIKnEupIvkb2Mpr8pa-27n2RFEVJE3YPNHaa-w0fwkQB6hi13jJVp0G3T9Vj8tRY0gbhLRP1oTSBD_acuGoB74pu_r2Z-TuLlEY1stOiXinDTdUcpTfZcss0McsfS1sI_KPXnh9DMX2e9kzvZlDdrGs8CMk_0eyR0-wdYfIp1M8EoJDMcFYZJp5NYfWmTY0qLYbAY1267EGqHiR5XEIPFEx9X5R2wsSkCYk33F3aInW6czN3Y1Cbv5RIeSX8qcYIGUFOXzWpxdKhCQvdTRIyinm5ObtjDYiU7jDYS335T0I7rS-A7yShmsHcsXN4-Nu0kJy6Pn42Fg9rTroNuGoZQ5w4UCAlUlVj4oBK0OLbLa8QE5JBI2WUzYyEnXLODzGqS2Z5-aGmKm-yWdyB_j7v4md5SzDs08ZPyXuTaH03O2UmanAVzFkoakMGotlb-0VTRr7VFLqqAd7b-M6roAtERKsXV74hmGDSotl7kkP-YDcb9gP9526F9ZqHcc0Dw1I8lFYtQD29fORXGquYZf9ysNny6z406-v-skSn2NkKwYdDM3Uu7eMfHWANJ4JprmVzA8hn63ijrKgoh3t6eXQy4oTz8iouiDUskvKP3YYQ7aLFsvV7TsSvVDN4eTeie9s7ow-3D6HbHJNQwkSTDjVLQqLJGZgB_to4L4lpc1WamwcjxPrHOqkmmuC9EroDsmnPSTw3WrEqoqZhLjrXlCk1KjZBB-SBl1jA1Hd1gs_EaSublPCVtZ1Th01E6qkefpJ0JGkdUVHgWwzUNVbFrsnXU1NbXu_F_zhigM8JuNRgQs5Sl-o82ZqN5Wg481rKUohxBOVrQ_14HKG2yWJ7mIdNhjOgKI1Q7OaFC49Y2r94BO5jKYrAlrupISpWJUqgiLOXbjdKiLijI8Y-ZSIZU7KxfzuJOOnrS1xEtM7DWF3h9bsoATMIXADErh2nCGf5d0cxtaNPIbRmC-gFy04_ie2wZ2fRJYtMkQFTeA9UuI0PL6GM9Y4r7jw5jX9vIiVAcvWjaq5x0kGpBiicXbXCLFOSGRnWtwS1eowwKtQYnCQPtBQA9jNW8Bse4EEPKmOc95L-wmLFNrCBX58-daHyv_CbeYaI7TWz31jqektCy6Ox9HNSmZuB_68O7r4AnzBJY5ebO2FHTEg6cyhndopMUQFMWH_OuJupa8AJJJGsI1OBn0V1-02iGc4gm69eOV2OTXBLTYRsb4cPITHiwz-Qmw67S5vPlR15GmZIMAadA9OauRRoEmjtEAExGWPp-ox8VQuXrA5R_GUYueVLO-zPjbm9S0IBS1wUVO2eAzah9e1-T9oJ5iuVOlOeMiLlSahOW-gl_CXH0ZRvn8REGPQkxO4je7Ji1Ib5pRZjDs6uvEJxSJ2QBbUJ_YtMLawVfOZHMcTsXefAAKuylAEPiAI2GFhrsMpzW6GkT0QoFfC6s4vHEXrIA9bF2tsMDEADCIObgIWyPxjFtghpT-cOz-EYOKoEy417_dr162Ux2b0GuF6o-ss4_1xsW0X_g3ukUTbfwSs2RQ2Wk3qj2m_ZCJJ1DjvaSAOgnHNRFupwY7Kn89ZKWaKctekk8SleCAIwOTA4KJ5dweKyuR2S776Rrqiph-QGxtk8OVOiCWW8hiiwJPgSd6_yGIGSC_0K_2OChjyDSEqEjU9XJaQ_KKrTq2CJo-tEEfRSaVX55DxeIVc9SjexTJHOGEVCtdpyu25J7iGLlIR5LQ758fo1gEQcf4a2zxUu_0wVRK89n7fldBC3JQDqVOdSF5LToZVzplg4dbYV5-oCiK6w-OXhM8R5xTQ7H5HuPoBZ8TKzPLPZvlXfjEf7VQP2j_2QyaBvvF_39s-8iU5my0khrK4Mv-lJRhD5X2ULhOIUu-LCS9qUyyEC5x49yKZZSg_IkvQynFRExUnz_zqgxaoYWxdsAth01RYKxaQ2m3gzRtsX39e0W8_2eX7VAnPIhmdwgctAtSFQx32Ia4GyoyTgRiRlEeDyXNq3r_nxih2gDT-_EHAOz4DYeBHqFILcfJqKFzrc0PWPu4U_LpKJKDxhNgC6mI_v_3nzfllVeMkbYmjkl9IT9DrPvsQQibiRJ33F5ep7UNdAFG-ucq-oz9-yWn0gsa4tBNjyM4YEJZgHia_JEnDcuJjysjbc83LINZhb7Dq4aZ37jrjRJ9pC86lgaTvXoT-Q4lMgIyEfwkWYCk4Eu1AEDgu5pY4yvCX7yN5vR1LRvwA8Q.6pETs0rnHVPUUaaXjvvDRw',
    # ]
    session = [
        '2B926DC9-C9A6-4CD9-8534-A75792C70A33',
        'D98BDDA5-213C-4D8A-8E14-99CB77E1AC4D',
        'D2C8649F-27D6-49A2-B9E8-DE58CC1F8B1C',
        '90B2A58F-17FE-47B9-BFE3-A36896461B0A',
        '050F161D-AB5F-4FDF-B9A0-77F81FF12F98',
    ]
    run_num = 0
    start_time = time.time()
    while True:
        if run_num >= len(session):
            run_num = run_num%len(session)

        session_token = session[run_num]
        # api = ChatGPT(session_token, verbose=True)
        client = Steamship(api_key=session_token,workspace="gpt-4")
        database = get_database()
        generator = client.use_plugin('gpt-4')
        # collection_ytb = database["ytb"]
        # item_details = collection_ytb.find({})
        # for item in item_details:
        #     filter = {'_id': item['_id'] }
        #     for j,comment in enumerate(item['comments_infor']):
        #         print(j,comment)
        #         update_database(filter, collection_ytb, False,'comments_infor.'+str(j)+'.check_flag')
        app_data = ['news_data']
        try:
            for app in app_data:
                analysis_data(database, type_app=app, generator=generator)
        except Exception as e:
            print("Error: ",e)
            run_num+=1
            print("Change session {}: ......".format(run_num))
        
        # cur_time = time.time()
        # if cur_time - start_time > 3500:
        #     break
    # collection_news = dbname["news_data"]
    # process_index = collection_news.create_index("check_process")
    
                