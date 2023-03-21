from pyChatGPT import ChatGPT
from test_api import *
import time
from pymongo import MongoClient
import urllib
from dateutil import parser
from datetime import datetime
# from timeout import timeout
import errno
import re
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

def call_gpt(task, input_text):
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
        # print("Prompt Abstract: ",prompt)

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

def combine_analysis(filter, collection, input_data, is_topic=False, is_keyword=False, is_sentiment=False, only_title=False):
    update_position = []
    update_var = []
    # if news_task:
    #     process_text = input_data['description']
    # else:
    #     process_text = input_data['description']
    if is_topic:
        print("Topic")
        topic = call_gpt("text_classify", input_data)
        update_position.append('topic')
        update_var.append(topic)
        # update_database(filter, collection, topic, 'topic')
    if is_keyword:
        print("KW")
        keywords = call_gpt('key_extract', input_data)
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

def analysis_data(database, type_app, api):
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
    item_details = collection.find(
        {"check_flag": False}).sort("time_crawl", -1)
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
                api.clear_conversations()
                #Sentiment text cua comment
                if (comment['comment']!=''): #If comment != None
                    if len(comment['comment'].split(" ")) < 100:
                        # Extract key information from commment
                        keyinfor = call_gpt('key_extract', comment['comment'])
                    else:
                        print("Abstract this comment because of too long")
                        comment['comment'] = call_gpt('abstract', comment['comment'])
                        keyinfor = call_gpt('key_extract', comment['comment'])
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
                item['topic'] = call_gpt('text_classify',item['title'])
                update_database(filter, collection, item['topic'], 'topic')
                #Neu khong co Description
                if (item['content']['description'] == ""):
                    #Tom tat content
                    if (len(item['content']["text"].strip(" ")))<6000:
                        # print("Length of content: ",)
                        item['content']['description'] = call_gpt('abstract',item['content']["text"])
                    else:
                        print("Content of paper is too long")
                        item['content']['description'] = item['title']

                    update_database(filter, collection, item['content']['description'], 'content.description')
                
                combine_analysis(filter, collection, item['content']['description'], is_keyword=True, is_sentiment=True)
                item['check_flag'] = True
            #Neu khong phai la bao'
            elif type_app == 'facebook':
                try:
                    combine_analysis(filter, collection, item['content']['text'], is_topic=True, is_keyword=True, is_sentiment=True)
                except:
                    print("Abstract this content because of too long")
                    item['content']['text'] = call_gpt('abstract',item['content']['text'])
                    combine_analysis(filter, collection, item['content']['text'], is_topic=True, is_keyword=True,
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
                combine_analysis(filter, collection, item['title'], is_topic=True, is_keyword=True, is_sentiment=True,only_title=True)
                item['check_flag'] = True
                

        print("Current flag: ",item["check_flag"])
        update_database(filter,collection,item["check_flag"], "check_flag")
if __name__ == "__main__":
    start_time = time.time()
    # key_infor = call_gpt(task='key_extract',input_text="GIA LAI Cú dứt điểm từ hơn 30 mét của Jhon Clay giúp Công an Hà Nội gỡ hòa 1-1 trên sân HAGL ở vòng 4 V-League 2023 hôm nay 19/2.")
    # print("Time: ",time.time()-start_time)
    # print(key_infor)
    session = [
        'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..fLmc3uZQJKV4e4SK.NH72XwaMXvEGymxrpLFcj4y6kb9AX-BJmhysuVhb3AOOI3TgO9GzucjVuO7a7sq4z2wbXr8CKR0XTvv3TybcYkL0IU46MxXMUxh1bO_Xdfo0P43H9-Ekr8bmPezIgWNsf2Y0-sm-SR_QBE2gjlU8613-J7V9XoOueIQTZ1f8CW4i-vTw94cAzQD1TTPXC8-qzyOhJiyBjmQrkPcB6KRCuIvOKP-2bxQRl-sWlrplCeRZfu_yeGJXjZ9lhHkTNsfBvd8QgHBiOtwJxZgx1nW-cpeU2VeQ4UDyuoeaRR3f4akKpP9SRH3YrsbacDzbb2aHQGfPsq46FAy5ErrXnHIErIVsj-jXdCVdv__sEiEOMthcABSvq6o-xonW6-AYPW7e_pcngetBzPeJgiD_nRyw8m-4f9F9JS_mIsPtRK_95gXANRrkoQKDhQ5k-zN9BucNrRBJybiFpx14xPMOF2K0qvkGLM5cEgIxUiDyh9qcdwK5TStY8fZ5rcCO8UB-hxVlru68Qnwotzi2oc-urTx_nrAXsfBysN1dMOWmJ191IyvnOjRU9ssidHKAEPCEeNuKZ2w0a34MaWy6xSElkrIaj7GJbzZHv7430rRY6Fuxk153pD5f87_5UdDS_KWeJBy7gfDvpNMwCBsAQqp4lBQM9TlPEEOaLav5hbM2PigxokHD4W-uYcI5ztbCJ4a4mAiHQuPbATIUREpmLeEKVmVoELtfFNbJQimwh4DNtfsifSvB01-zZyK3nU7HQvD3vcRC2lD0zEbng_P4seHuRF18QjvBHGGhSb6e7UTBU9eqknB5Jiw-zIGwIc-VSdWWlNOsuN7Vatle21GKhkU2llwrNvrpgMWQUxZs9dfH5YnDnG-SVE6MGHPDFQHPw2Bnld0dDufLlPpbhnLrqwlSDDHn8rXNiS6MXegaFwLWJoUqAZHtqaTy_dqf6NNsc6YM_SAOa803viZAG62CB8TyQIpgE32GB5T099Lf0-dBQCiorAyB1tOsSwzCKkOG1UGYF_49RBDv2Z3VXfrL3aa15z2UBjrjjMfv1PQqc706SbwKcdR01xqseIEmHnCoSMqRE-sUMFjfMoukqy_pjQRJlOOCGDgm7Da6Sn-3s-OqwCeSWb-4dCFCuGn1S1QZs0J2DzxFSv5OSZCxmdCFRtIDgxr4KMP-iI30fFv_YZq_1Bu2DGElzgC8mXmeS1BWwMuWrfs9ferhp2WOd6Bn-mrSWG-48N-Pnj968VfOjhU3-IaMfMu7lUkvHj2mxzJaSL0Y4KosjScgn2Nj-6uGKWTL7jEyIGaP_4-9YUjQjV4yH_FHNuWRudKxYXfmKKErX806_UfS9-LJGkejirCDVelw3DnWUDaPIe2YMUj8wDn-KDcFZlHJscbC7dEEQC6ftprqk4KirPDuO0eKEAa9QYpGLqihm9d3F4CHti-ccvDFk48Hej2O-FJWm0WfLUL9cTq11_vUSxRLfrjpNBxErmP4dAg8_ZT8or034BDrr_tfN3zpLLU7dLiIbugy6qAnJzg5soHKvLB-x-W4tXFLpEwlymyKxKNWtOqSJVkOmYXy8hi7fX33o-h-lK8aTRMpu7AT7UJJEdzRhssElDyDTqx65PEEceTzUtuMsLt8v7Rx-yrkI42G2Kx0fickUwX4grz_VddhlCw6bSSNShAThdol4jOG4CMZFdPe1UDyHub49SSBZ53RTJ1xyXzF6LDSEcsxjH9R_TZhpdvkXdGjiEFHofG86s9_1cw1vZuoDct0KsGvTmxkcUtCRleskCB_TMNXMT4kIBR54Uk7D_yphMpDtZE27Wnb7YWCLXFsL0nd2Fm7wIjcKYfyatXjXGHlGPny4_KFVXIozzsxKGCyEWg0gwzM2srztuYb8F5cltIzeDR4CYhuLKSmOcC-c2NrMoSBNv75QCRUxtp7yVMFdNK9xddjWldr-q2PS8PcJzRuGbRtEQ2An6y6yxnJqptiSREghcL5cJI3Nh5utDCoYLMLs64rbWbDHnDizUDCM1dOT3OqJFbwLNEJASNwG7vYN9YGAOzcStw7KUpNfvMGNfd8bhtLOm3OI6ryOkMA0-7gFGuhx6ImharCYUhV4oY-wQDUqaYBsW1Onj6QVjh0aLyDnmuztRua7UnibY1O8cUqhTOot7l1OuVVX0bdjOFJU1HAJMRxGeuRjMd0dEzatJvuu-Y3BZruVLgA_OV-MmS0IKHgDZVyG6zN4VRw9m7gSgugg8WLY3XENAuEl80ETjUMu3cWRJceqeTgeYxKDppEsAQHX2JcnRSt4rPT5mtGBduX6iHdyTbwZEm9Prdx9oQiTYjVNV-Up1OEbgUM2E3H60rYbLNHlOkEN3afHNqztLhTlynN3zgj42aXhVB5PilcoYNPo6IkRfCFPPYGy5_5M2i9YqabnfzF2wMkDaTUPAUycvDFYoVTN7tZqK0w10egEdlSigxEzWUHMuzS5O3jbtq5p0muatrn0y0xda_pG_GOpUsx_GN2TgQuH0Ur65r3fBMel83_a9N5W3U9DdQKL-AVGjAEllKy-F75ApqSMKTE-a_qYsYAWQBKkZLx5q3-d0w3uX05o7LMYrYhnuJj1asgsvOy2cRC-jW1EEEC5qBQ2_mHqFnDhUfaRK5vqEV_0JLTIKbx9tOUAaSR0wjONTGyZtN2BQqBB3TRStKoraA.AjGcg3u3FhUc9I8RHytDnQ',
        'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..6EFNeG5yt5nsc8yd.19EO5pNEUWgPOd0f1NNzUEeyHKVVHVOZf5oylGtoBttSFuLdPpk3rXGZvRKuMmPdCFn65NM5ndwxgDSfy3nS_TYYXsX49tnVEz_dPzQKBX_XMNbPgA7ZXt2G7O5F5sWSBdRxAuRcUzwrkj7NlU3dmW0GXwrY4LjNjWG-ha3xNNb8564NxxT9xrQQR3HHdMMwu_MeB0ASCeVBt40-R5_vKFdRlY9Pw1dgEHHXumqeiyECTGLXinbezn01PCq5F-j14-WAAZWhKSf5gjWi_yhoFSIw8mdpqZsCk7p_IO7i-1JKM5EtRFzrhr79aROpW4QJCvTBeSZ3w9ATEag8iWmsjCSnNaph0qAzpVbCUy1Wo16sER57SMmDMVP9OFERqvWLRvfUaDyzafs-OFa15pHSJL5idFEbEPDXxB_qrd5kx6BveDlOLnfeaZm8j3sqSqTMucx-KsbVF8ZLwljdXM68mBEmGMlPJrpMEPRrGdlsaSyLbcUNwFAjnKkdB1Kaz9YUKURJ1R352g0M3WAnH5VumFeziC-RlpEfqGGTeCWiaCTJgl1LgidEUmk6n1qfpyBEgDUkz9DbLfQPVFPoASqs-eEPIz-dKGZHlAM4QsTqQFBB94InSUl_gxpnItPNeC_pQCqEhjtMZGpBNWM-eKxFI3IBgDQ02kXaK6TUSmpnJJZHvuCMJRya5Q-i-QHeI4volo5rF3F3coZ9RWdnyPgGjjfNfobYemcfif-NkSoNqjgQBUPmKetfVwpXwGpnr-zIzcPHaQu594dgJ3Keks6GKU70MdrUz5BPw6o1xbzHxkFyatwi8s_QPP9IOueM91U9NqeRms6YnqM-QBMfrcih9eFt4PYnNXEoTWhpBTJs72YC05WkJN4ZScZUCM2e7ukm5q_FBN6dScR00kR9fK6zQvGx_gJ9FwI2_e_xDND3jXrZTS2zcvcZ-5ZndcYQsRNpIREFK7UUD2O9LmkyJJtqbNdI0ZQW2Sq5amrAYl2Z9n6h3ch07pLSS9GIr-Fyam3oMnDuAZlueYJ-8LW0laW-9EqgJkGb5kyNAEjEq0LcP0gkdn-FR_wqC4iKkAqNGGg__Quec__pWELNyDUH4oPXFHil9fJfoSG8u2RA9u5yrKHVabsBORs42QnwnqDsT6t1gJ3woQVUCzBdKPTKqmOU6nKM-uJHx_pnycVhs2r71usfae-8BuPH4scRPCpEFMlQdWi6Maf0Q7dHakyzpxeqJHQ_5xqquzny7cW4-0DBx7hznYdsigCgIKEdF1p_ZuBALv_HcvU5M9HvO7zREXgicii5HYmc6WB1Hg8D7_BrkxF584tpJ5HkHG566L9Ld5CgblojSODc2N7qZG_9YvdhotB06Yasn7qKIcmdcOi9hZYmgzJ7bnI52BKTHv1v3wexi0MdhWrJZsSJGaJlDgAqG3xiBxlWy3ifR8x8YWgSzcoJgUNowhnjIin_yOcXL3wgOyojVfawJkI3S7HnYAr8CnyKM9IJfmOpPhpkElQCebeO5iYeXXNjRoqh7y6NHBMPdaCgcd0tv1t8kIpYWTJGVufMSgUktSnqAmYb9_3KagWG9Q1-1jwFB9rH2qmwEP4eHXKxirF9cOGYXRq_eRcenpmFdvcWOkNaTJqWoL7Ejh1o31vAIzFUKshyXIrICw3xsOOWFlumIylmej_GAXYJgEG98YJp3980O8L1BXQLM3KVEN-bnKVR8CBskUSEmZ64uVPnXgWhV2XG0M-ccu0-Vlf7qH_aofU2UiZ9o5xTgrbPhAo17yln9-mY1UhQke_8OCfw-YETtnvHKqGiWV7kDOtOrLHpzIBEgIatDwbg26hFXqdOCEkPBPcPr1VdcC7LoNX6yZhz3BYjQBh7AptCNTHtZJE8dUROIC4Fq8bcx-7W4iehjn3_ifIBGOJ2Xa3hNSbCgGZGIK1etsTJipjtAbLWdkosLzSXzvBBYaO-Hqt5nj3nFPanrxZ2PRsVBskMDxbpyv8LY_9Ila7q-bmUtlIStpyZbnT17FdjqyoyFeVZmx5SsClYkourHL4SqWAQ2FVzUgj7JGZGw1dcESAV5YMWmK9ySz1FvlPJ4I4jDu85wO4n1XoYdrT8jjGSBfZnVj6T0Zyo824gXgq6o7Fggc0T0U_e27MCYKNbew6sEUj39T1sldPHSVpYAAo7_MYthLEfnLkIyBq6IDN1cjUnWZ9VS__iPej_2lyq5sfFgTRnXpr5-5qPBvmmjzoKqU8XJmjDPcA676Sc4Xv5dw5aYYRW1dR_68J-lXxVBj4pwzFC5dYT2YCISgo3L8QSueMQkow17drtdrt-H8KdaLh5D-UbBV1-XW0bcRZie72bu15IjuuaBiIsY94ygG83IGu4ZdvXUT7XjzwXCbbI1lxlID3oVT058xhYHJAzB5xC76CTV5pW7f_AkJNHOqK0qVZNRsf8dn_W5xVnEcrd50eQ9l6C4CdCydXJJI38OxdxQzgk4k8FzDQswfMP-MP3_pocKuljB2DI6Hu7aqRYAP-HPuAJfN4rbKw-uKoFKT2V7UxeduWFwsvHF2wJZRGYKQzWzX5j-GC6a8VUKgaxxu8AVsAxfaOrLs8yeGwhXfqYLfkDfpCpQZHZ6XNsvlVS3Kjo8UiONDCJv1PBmopvNf4bO_DUG6oFLiE.n5JT7qXmTlvSCj-eRahC7A',
        'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..EsfQfEJ3OeunVuGV.-GuWOEvV-yROCmneKf0w2OELjI_CFfFMFFczp_1IE7qhLD-qI0iLjgUQKfeIL3r5K1qHGZXNzpDhZ27N-q3JNwsqLKLpmXXHZJDt5PDqCNpT2MAlqL_9lTkZEsxyzWINI1s07v8IRyhiDNZqmPjq3GBvMY1pc1u7jAdzH2sZXSVSmbiBDpFJv7x-HUjIFIkS3SaLyBlO1x8_KcN070PZDrOBQTV0iZWAZ6t-PNmZ9iiCNfhBjXl1ksck3RGIQGn1djgTKXENPyRwpaL05tvHy4QOtYueRxs4kgirXzDTeonnP-zCXhFKSmYrpKn1PHqCWg24lkVwvSsC6LADXBlbYZMZGFMVy7AGdjw-iw7jJ756v2j_LKdbknPDjLoAi6mS6gkpY5gNppF0IAoNDpBF-VaxR-wjj0NW1UtHshG-hblkTkMZs_T9xbbb9U15o-bVHgM24tikc93dExM8KHf-L3NwAF7rl9mqylGXPYrJtUl3jRMhdyP7cqJdj5_RM-VEdM0WrkufFD4UGsiNlqO6QHbXTsH4V3Zz04rQN1jtAAdEp6p0_Q3aEpqDbU4ZtBTOQd9fh6TsN9R5q-6MvPdtVg8KgZWhf4mL93PL39knp9Dk6JTH-rUqQiKh58OTD3IyqsFCDTm0-acZfQg8rFJPP9NsFlwCaacqFdnGV4vroLjcmHVdQNjEBtE7kryZTRzpOA8OvObnJ8BGNY3VCDX2hP9-r7KHgtzliIWXmEvd_Z69e_ACBRo2hlEu6pQ7wLHIrl48Vsw1x-ewk_Q4vB17CtoGsDnvpSuIIfNZMyYo_YN2c3DCLKL43wwpR-Rd1JZvc7D6S8_FYQyB976r2sZH6TJ05nB0UmHUbIOtneG7fInC82VahJRPWdLLqwMwS0OPn_s4A6rQ_dATV7J9ESKTYnLuffMEkrqE6r8_nMGVNmvljlZ5oKwsqeIjA5satPGf3Af_cNl1vIXc6xXZLk3nqDyQsAqhryckR4wSLWlZc9FCyw6VHQn9ak9tDhx8OxOWfpOgDaQDY4lx8fCPouUIxXrj1moA-DSkXB0_5ZVlldWlAdlGiZLPfQpQAYQyOWTJgsPYx73AHlQF2_d5DwSr8Me5z11aaBrbmy-ZqHS3vwZNJUflrKm8Mis7ZEJ8bRuw7ycPhCN8u22ThRU1pHdMhiZ9IM5TRHfSgQqJzzrlmckiA56S77VDHhZGGHDyM8Rm3tdkb3B-KelaOcAbeFpZeYtAhC2vcnovU25BelZOPiMKdO-uD1PVU5T7O647qFMrTmrkHdAXyjzNLTupL7-H5uAPLbhsxX8g3a4ag6K1snoqNnE4yiialwj9_dfjCtUYrFiPiaRJ8dpGQPvG5shyxhQLzPYOue5FI0bb9Wxjo02geDq_bMOqycI28pHwUQcllk11ExVDng1JftTCRJxc1OrixjmJXGgvXW9qKEtl5juoiWF5vMjYZEtdYIaN3C8obTZNT7glrCQWPa3lISNPP6ujGbNN8fIoSjFAzH1VXaL7qLzjsY6N4hA5yJQOAmDJPyN7qD9ad3K3GSaAeS7NmGzQsDoqe1gPBtGMXkFfKXWp3xGU3_vGI1K2YG-_Ode9TJL2-mZE4ECMQH1xhTRI6PjfnYHTeKhjJ1Wz9v9_vIUe2F4U5OtBoNJrizqbrcKMX8B3ROOV7-GydGYTIRjX5VvFqNkRiQmXq5pgB93Ge0iST0MIY_SJN_LtiwP84KOox7m08K8IOI8uPO2F0x9_WEOl5ctHqPX-6eXYaKNpApybY8G0J40qpnIUQbYy1WnUU3QK7MnY4EJZKnw2t3bvf_Pk8wByH-Bp-a1mvymcnDwsoaMgt4lBH-psOLw_Bf4vw5ia7WLB2jbkgdYz0j0OvBHyFRRMrqsYv-yfAZLAc5Yxz9Rb4eJKUgzc3VQeTF1SUkHvDeT1aAuoHikQs59SI31PCYDQHTmGaHDXFBYSzLGEj4K3KQyMR9150rADKk37Tbz-QThcqEhcvXfPidUV6m1gd9LFxeKw5CuHjigzL8k2UimB47dk2x_i4cWdNuMF7ANOSO1eP1P7N9M11T_kwKEbLaeLUs_biLVN1fZs99rS7tClbDfaOgy-a-TGJmrFZJHQKhNqKySsV-0hGN76POQKfL2qSaFKthRCsxTI5fRUbbbt7YepmAitk4xcOpiyXdn5DURerKHEXxNK6WyJVyxzzXPCrZuwvQ7WdaOiIat79efJ-rNhR9S9HFoBVDVGZtAWa92WIiJoaK2DotHj0TAjhHVSYBGigtEDoF3bVk926okHZWGx65yszsk05oTC8P1Zt-paeFvsb041XknlkSUjrAAFAxPdn8bYMo0SRYQLrOYhhCVcySwxZW915e69Nlzo1eO11O37U3r4_KLLgIWrxT8HqMm8USDmWhbbNAQ3ccrSaOxIYGE3mQRZHWkKQG1Avmfqw3uVeZoREdh3dzSjxWKJxJ3l4bpCeihev8b7biO72jKYMF1dEhjhwyfqS6ej5iUv2TJHpQRqkbGhoIAWhavDzkhAPgiwIWfWWCtbs0ycoZysoccBTToZMpIUJ47LrkEAc8dlZl_88MyoC7it-Pdp48EXp-_fARmxzmidkmaaWvygnt7NWPsF-ntbxPhVyiLVRjVtFRK2t4oWZG6IAPke45fk7UKOugT7z8G6Mw.5qH_nRCK7xnsnGrou3FoWw',
        'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..NYQDTRZ_vkfDb07i.US6KT-1irtnAJPuIpffFZEUHkBmyZovc1azv4JBvub-hF8rLKhmXCHKEcLvWuO3P1YvtN4FFbSxpNgJFccA3r_eihjZIp5I1Pn8dwQ_JIxZ5fAwu_twZtwl-Jsg6ZnnovTqAIW8ToNYXtY8GoCD_ASxXTfUnfpCEuZFLEwWU-sl6vBVgf-XCLUl-EdsX-HLqZZ3GDu_ZZpjwrf2grU3_aICA9FvuybP027T_A3YoqDxtv1zuUQ7XMjEOfjbNmG6CDWZqzXU4p6etpbIMkcBZwfFMw7aoocKuGrDEqeF0dxwEjUhkqD1lCPw5eTCaFDCHAl65HtV4D896_B93OPJEjhQsh0Ownqvfr5EDjj64QZ1OYHzDU85X7TjiHEqQtZlwdkrADg49AB_TAv0M7mQH2BxfoTWyZij_v-Xpxj4EiwaTaru2v89a4VeFeZayx5Zx5NT3Wq74sNpqPuPCGNgh3Vg2yrpEAGvlJF2fR6wX34IluFoUvIJ-HgryWTFHIQmPYZR3hbmaNFaCfItuMocULB_BpWl70xjFhLrSYpjqZTwDB45Py1W2l0BI-7wk9M-x7J4ExkbmzOE6y4wYJQDb1PfCCG4ly0EdqKHSuWRJky0xbWQL51TBhvqpstGuhRsdaARyxGlGiK3NVpq2oyHJAi4BVO3eRNm_JdraSB_YxGiTGER4V52MDDhL6raXyE0LNB7ho05oyX895OTaNS1P0QRkmIWzpFMGXeca_YgvKy24ABB0FqlWUelO3_FXYdfXShDEnmA_wl6uRnG4tmmVi6iz1y2X1j2c8dIar4mOQWyuBiJa227KIqsVZU7besBFUfYuzWWWTS-MVFPlFWA0_imDKbrDh5QXow0UKOarrafV6BWIEGYKpHn1WXhXvK-tGuPZ0g2rvQhUTCwdofdB0K7jxKCnoHs7PDoMDkvjxGaKKk3JI27QIF1bsqdsNdPWrVreW9EOInUbsYwwE0u9VHsUK6wxXdyp3ZfzDvRhsPhZl_C2Lz42NJ4tdfwxTchV_IIDSzd31cryt2dkuIe7XsRGvCw6_s8fbSQ2PYSErghDPmy05sAnF1P5Hk06jnvNoqub5ncSWig8NQgDma4Q_xnIJMLiko2YabClA5dOUwM0bVwnwoWgn4kQCmh7ozKaWrG_UyWKUyYQbLzUce16O0udqjFo7fdAqrElxypdm0G836KV9s2HAt2An6sVUUQofLfScY9MruNIVM6o-kwJJFJf0-0R5i8kP5xquUCqy0tIXYMfbNGU7fcINrlq-w7Ph58EHSvVC8MebYH5ARns6L5wzhjw-QCWeRJ-tTHHnbL5bi9Lo4vqBTbD6jCfkS7K_xSnpeN_ErYmKIxG3SzoKc8pzbaq5qQN6ytuXs5oBV6yHd97HdQO6VPuhleIIp2yjGmw_H2SfvAzsW2Iu7GoEFkpyUNUxxkQ2HpNmyeKDyyvRjO4FleMVCwF0l-aq9P6RBnIJepbiVtxh6qh-GdTiIIqXBU0Jnw5UDb985x7nQuHCudPXPlWAQRoD5aQ9i4UEtttgFnMgy5uDTunU2AJneQwftBgmUyPfh_MmPfyJ-Bk2rG8-XZtfbv7szxCJqN1N61qlhUuJ9S9l1BVBb0v6kfu3vfmO1slSbkI_3DDMTcMfXrk3ynJsjU1n4zkh4YtmSHgtVA0Ex_MRauTIGoImtYnMB6zEdDXLsXFW5Ua2qLYnAM5mTIenIEG0NamxZylrWNMo2b2kxtzwyKLxzEJTYkLuuahkqBiR1bl5Z9gtXDwLAUR5xj3xxQMPDR_JXTkOu5Ob5uRD8uf0LBQou8MsKXWpPaiHOxuGBY_-IyN1fAivyA3QOPAecsG-c7Yv-I5xrkp8GgyRXKdlWK7vYdk10QzqVZ-TPsfvAQEnu4GGy9lyLDQkt7w86e6XcPkUIqkXjs-yKJVuOmGOMwT0KywBFfEf43kxSP5E3kvbui3Dj3t2wrO24dQU3mGEApNkApd5pgZYHo0hFCBtLfvnyrxGwrwebpA7c9ZzVSCXAz5hEyDC6CrGg0qRx-xPjvi7u3XxniJtnQknf3t7JJAkHH2LOy_O6bvgP4F3r6fUwxLNI7DhCUzCH9TyWTGil0IZhhX3JZyRjGkdDNPW09LkoCGirb3g5Gg1Pr7gZtbvdIfQycV_4OSnDUDN4d4VmHmfvENTRL5rEA039ffoYQ1mrK1SVdXGbcDN6w71D3SfHDZOCZBQEKpoSB4x1SVj-g3sm-99jgWIZ8CjOqNBveXmkOFhMaC8aWYdVWlJK99Vcyai4CqDXmrDnIPO-QtQJdHDVaDVlzhoLdmKVxwceqiRA-OqAFjgktK_UgYZ1qf16aKYEQzjAM9ZW58ro_WGM929Vew5LOW4b9F4QnednRNmVQb0LvwnuB8Wk8CXtyXSObRtOrkxnqv3zlC0YTz0xkkjPSlf3dSLOazsjVvsH4tfCIBlbC6YcyZXbKOR-NM0wNcKd5Rs7jnil0taXteNfZGTh1sizscAKt8y-2E1hZAwjwmJ__pBg3uD776O1sBWLrMc9PktAwu2x-_KnDWElArPhaDbpcDk6fUbI1vmgPMsrnRO5PCwco35SlMGk-g9HQ79WCdGlQAawwop1kLGA2l_4M8ozFXpTyd9keKvlR0sFMfj2tIZhtivmIUmu1s2g.RrvS59qyq6ezEL5vF0QvOA',
   
    ]
    run_num = 0
    # start_time = time.time()
    while True:
        if run_num >= len(session):
            run_num = run_num%len(session)

        session_token = session[run_num]
        api = ChatGPT(session_token, verbose=True)
        database = get_database()

        # collection_ytb = database["ytb"]
        # item_details = collection_ytb.find({})
        # for item in item_details:
        #     filter = {'_id': item['_id'] }
        #     for j,comment in enumerate(item['comments_infor']):
        #         print(j,comment)
        #         update_database(filter, collection_ytb, False,'comments_infor.'+str(j)+'.check_flag')
        app_data = ['facebook','news_data','youtube']
        try:
            for app in app_data:
                analysis_data(database, type_app=app, api=api)
        except Exception as e :
            print("Tat ca tai loi",e)
            run_num+=1
            print("Change session {}: ......".format(run_num))
        
        # cur_time = time.time()
        # if cur_time - start_time > 3500:
        #     break
    # collection_news = dbname["news_data"]
    # process_index = collection_news.create_index("check_process")
    
                